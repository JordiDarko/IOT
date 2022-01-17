from django.urls import path
from app1 import views

urlpatterns = [
    path('rele_on/', views.rele_on),
    path('rele_off/', views.rele_off
    ),
]