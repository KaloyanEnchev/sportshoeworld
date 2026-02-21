from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountDetailView.as_view(), name='detail'),
    path('delete/', views.AccountDeleteView.as_view(), name='delete')
]