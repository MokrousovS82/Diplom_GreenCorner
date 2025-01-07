from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homes/', views.HomeListView.as_view(), name='homes-list'),
    path('homes/<int:pk>/', views.HomeDetailView.as_view(), name='home-detail'),
    path('fishs/', views.FishListView.as_view(), name='fishs-list'),
    path('fishs/<int:pk>/', views.FishDetailView.as_view(), name='fish-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
