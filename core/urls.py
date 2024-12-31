from django.urls import path
from . import views  # Import the views file

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Add this line for the 'about' page
    path('contact/', views.contact, name='contact'),
    path('job-board/', views.job_board, name='job_board'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # Other URL patterns
]
