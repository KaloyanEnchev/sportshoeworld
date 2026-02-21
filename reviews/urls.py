from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    path('', views.ReviewList.as_view(), name='list'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.ReviewEditView.as_view(), name='edit'),
    path('<int:pk>/delete', views.ReviewDeleteView.as_view(), name='delete'),
]