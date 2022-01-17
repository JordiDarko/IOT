from django.urls import path
from app1 import views

urlpatterns = [
    path('rele_on/', views.product_list),
    path('rele_off/', views.order_list),
]