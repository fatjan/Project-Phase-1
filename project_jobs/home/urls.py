from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home, name='home'),
    path('about/', views.display_about, name='about'),
    path('category/', views.display_category, name='category'),
]

