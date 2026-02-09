from django.urls import path
from . import views

urlpatterns = [
    path('marketplace/', views.MarketPlace, name = 'MarketPlace'),
    path('<slug:vendor_slug>/', views.VendorDetails, name = 'VendorDetails'),

    #ADD TO CART
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name = 'add_to_cart'),
]
