from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = 'apple_home'),
]




