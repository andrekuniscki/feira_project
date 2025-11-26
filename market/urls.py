from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('items/', views.ItemListView.as_view(), name='item_list'),
    path('items/new/', views.ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('about/', views.AboutView.as_view(), name='about'),
]