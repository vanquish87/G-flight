from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerAccount, name='register'),
    path('login/', views.loginAccount, name='login'),
    path('logout/', views.logoutAccount, name='logout'),
    
    path('dashboard/', views.dashAccount, name='dashboard'),
]