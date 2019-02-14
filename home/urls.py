from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home, name='home'),
    path('about/', views.display_about, name='about'),
    path('category/', views.display_category, name='category'),
    path('jobdetail/<int:job_id>', views.job_desc, name='job_desc'),
    path('job_post/', views.job_new, name='job_new'),
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up')
]

