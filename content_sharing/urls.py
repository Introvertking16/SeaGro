from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='content_sharing_home'),
]
