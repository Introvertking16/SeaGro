from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('profiles/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('job-board/', include('job_board.urls')),  # Job Board app
    path('learning-center/', include('learning_center.urls')),  # Learning Center app
    path('community/', include('community.urls')),  # Community app
    path('bike-sharing/', include('bike_sharing.urls')),  # Bike Sharing app
    path('tech-news/', include('tech_news.urls')),  # Tech News app
    path('chat/', include('chat.urls')),  # Chat app
    path('content-sharing/', include('content_sharing.urls')),  # Content Sharing app
    path('todo/', include('todo.urls')),  # Todo app
    path('about/', core_views.about, name='about'),
    path('contact/', core_views.contact, name='contact'),
    path('login/', core_views.login, name='login'),
    path('register/', core_views.register, name='register'),
]
 