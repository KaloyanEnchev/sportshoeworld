from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from reviews.forms import ReviewForm, ReviewDeleteForm
from reviews.models import Review
from reviews.tasks import enqueue_review_processing


# Create your views here.
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)

        transaction.on_commit(
            lambda: enqueue_review_processing(self.object.id, 'heavy')
        )

        return response

def normalize_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    try:
        enqueue_review_processing(review.pk, 'light')
        messages.success(request, 'Review normalization queued!')
    except Exception as e:
        messages.error(request, f'Error: {e}')

    return redirect('reviews:detail', pk=pk)

class ReviewList(ListView):
    model = Review
    ordering = ['-created_at']
    paginate_by = 3
    template_name = "reviews/review_list.html"

    def get_queryset(self):
        qs = Review.objects.filter(is_verified=True).select_related('shoe')
        review_type = self.request.GET.get('type')
        if review_type:
            qs = qs.filter(review_type=review_type)

        search_query = self.request.GET.get('search')
        if search_query:
            qs = qs.filter(shoe__brand__icontains=search_query)
        return qs

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review-detail.html'
    context_object_name = 'review'

    def get_queryset(self):
        return Review.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_reviews'] = Review.objects.filter(
            review_type=self.object.review_type,
        ).exclude(pk=self.object.pk)[:3]
        return context

class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review-edit-page.html'

    def get_success_url(self) -> str:
        return reverse('reviews:detail', kwargs={'pk': self.object.pk})

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    form_class = ReviewDeleteForm
    template_name = 'reviews/review-delete-page.html'

    def get_success_url(self):
        return reverse('shoes:shoe-detail', kwargs={'slug': self.object.shoe.slug})

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)