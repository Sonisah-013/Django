from django.urls import path
from . import views

urlpatterns = [
      
      path('', views.homepage, name='home_page'),
      path('dashboard/', views.dashboard, name='dashboard'),
      path('profile/', views.profile_create, name='profile'),

]