from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = 'apple_home'),
    path('apple/ad-ipad/', views.ipad_detail, name='ipad_detail'),
    path('apple/ad-iphone/', views.iphone_detail, name='iphone_detail'),
]




