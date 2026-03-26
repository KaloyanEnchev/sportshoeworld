from django.urls import path

from api_shoes.views import ShoeListCreateAPIView, ShoeDetailAPIView, ShoeStatsView

urlpatterns = [
    path('', ShoeListCreateAPIView.as_view(), name='shoes'),
    path('<int:pk>/', ShoeDetailAPIView.as_view(), name='shoe-detail'),
    path('stats/', ShoeStatsView.as_view(), name='shoe-stats'),
]