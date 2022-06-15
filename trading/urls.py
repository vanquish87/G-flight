from django.urls import path
from . import views

urlpatterns = [
    path('api-status/', views.APIStatus, name='APIStatus'),
]