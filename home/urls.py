from django.contrib import admin
from django.urls import path
from . import views
# from .views import HomeView

app_name= 'home'
urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
]