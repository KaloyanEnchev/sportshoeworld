from django.urls import path

from common import views

app_name = 'common'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:photo_pk>/like/', views.like_functionality, name='like'),
]