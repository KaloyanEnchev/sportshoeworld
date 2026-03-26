from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView
from accounts.forms import AppUserCreationForm
from accounts.forms import ProfileForm
from accounts.models import Profile
from common.mixins import CheckUserIsOwner

# Create your views here.
UserModel = get_user_model()

class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('accounts:login')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'


class ProfileEditView(LoginRequiredMixin, CheckUserIsOwner, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self) -> str:
        return reverse(
            'accounts:details',
            kwargs={
                "pk": self.object.pk,
            }
        )

def profile_delete(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(UserModel, pk=pk)

    if request.user.is_authenticated and request.user.pk == user.pk:
        if request.method == "POST":
            user.delete()
            return redirect("common:home")
    else:
        return HttpResponseForbidden()

    return render(request, 'accounts/account-delete.html', {'object': user})