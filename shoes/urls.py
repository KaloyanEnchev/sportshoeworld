from shoes import views
from django.urls import path
from shoes.views import ShoeDetailView, ShoeEditView, ShoeDeleteView

app_name = 'shoes'

urlpatterns = [
    path('create/', views.ShoeCreateView.as_view(), name='create'),
    path('', views.ShoeListView.as_view(), name='list'),
    path('men/', views.MenShoeListView.as_view(), name='men-list'),
    path('women/', views.WomenShoeListView.as_view(), name='women-list'),
    path('unisex/', views.UnisexShoeListView.as_view(), name='unisex-list'),

    path('basketball/', views.BasketballShoeListView.as_view(), name='basketball-list'),
    path('volleyball/', views.VolleyballShoeListView.as_view(), name='volleyball-list'),
    path('handball/', views.HandballShoeListView.as_view(), name='handball-list'),
    path('football/', views.FootballShoeListView.as_view(), name='football-list'),
    path('<slug:slug>/', ShoeDetailView.as_view(), name='shoe-detail'),
    path('<slug:slug>/edit', ShoeEditView.as_view(), name='shoe-edit'),
    path('<slug:slug>/delete', ShoeDeleteView.as_view(), name='shoe-delete'),
]