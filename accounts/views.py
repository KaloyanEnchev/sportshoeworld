from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from accounts.models import Account
from accounts.util import get_profile


# Create your views here.
class AccountDetailView(DetailView):
    template_name = 'accounts/account-details.html'

    def get_object(self, queryset=None) -> Account:
        return get_profile()


class AccountDeleteView(TemplateView):
    template_name = 'accounts/account-delete.html'

    def post(self, request):
        get_profile().delete()
        return redirect('common:home')