from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tech_news_home'),
]
