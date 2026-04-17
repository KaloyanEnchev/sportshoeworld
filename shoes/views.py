from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.choices import GenderChoices
from common.mixins import SuccessMessageMixin, RecentObjectsMixin
from shoes.forms import ShoeFormBasic, ShoeDeleteForm, ShoeEditForm
from shoes.models import Shoe, Category


# Create your views here.
class ShoeCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Shoe
    form_class = ShoeFormBasic
    success_url = reverse_lazy('common:home')
    template_name = 'shoes/shoe-create-page.html'
    success_message = 'Shoe was created successfully'

class ShoeEditView(LoginRequiredMixin, UpdateView):
    model = Shoe
    form_class = ShoeEditForm
    template_name = 'shoes/shoe-edit-page.html'

    def get_success_url(self) -> str:
        return reverse('shoes:shoe-detail', kwargs={'slug': self.object.slug})

class ShoeDeleteView(LoginRequiredMixin, DeleteView):
    model = Shoe
    form_class = ShoeDeleteForm
    template_name = 'shoes/shoe-delete-page.html'
    success_url = reverse_lazy("common:home")

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)

class ShoeDetailView(DetailView):
    model = Shoe
    template_name = 'shoes/shoe_detail.html'

    def get_queryset(self):
        return (
            Shoe.objects
            .annotate(
                likes_count=Count('like'),
                average_rating=Avg('reviews__rating'),
            )
            .prefetch_related('reviews')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        shoe = self.object

        context['likes_count'] = shoe.likes_count
        context['is_liked'] = shoe.likes_count > 0
        context['reviews'] = shoe.reviews.all().order_by('-created_at')
        context['average_rating'] = (
            round(shoe.average_rating, 1)
            if shoe.average_rating
            else "N/A"
        )

        return context


class ShoeListView(ListView, RecentObjectsMixin):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')

        if category_id:
            queryset = queryset.filter(categories__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BasketballShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/basketball_shoe_list.html'

    def get_queryset(self):
        return Shoe.objects.filter(categories__sport__iexact="Basketball")

class VolleyballShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/volleyball_shoe_list.html'

    def get_queryset(self):
        return Shoe.objects.filter(categories__sport__iexact="Volleyball")

class HandballShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/handball_shoe_list.html'

    def get_queryset(self):
        return Shoe.objects.filter(categories__sport__iexact="Handball")

class FootballShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/football_shoe_list.html'

    def get_queryset(self):
        return Shoe.objects.filter(categories__sport__iexact="Football")

class MenShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/men-shoe-list.html'

    def get_queryset(self):
        return Shoe.objects.filter(gender=GenderChoices.MEN)

class WomenShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/women-shoe-list.html'

    def get_queryset(self):
        return Shoe.objects.filter(gender=GenderChoices.WOMEN)

class UnisexShoeListView(ListView):
    model = Shoe
    paginate_by = 3
    recent_results_limit = 3
    ordering = ['-created_at']
    template_name = 'shoes/unisex-shoe-list.html'

    def get_queryset(self):
        return Shoe.objects.filter(gender=GenderChoices.UNISEX)