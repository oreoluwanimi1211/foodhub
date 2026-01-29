from django.urls import path,include
from accounts import views as AccountView
from . import views
urlpatterns=[
    path('', AccountView.VendorDashboard, name = 'vendor'),
    path('profile/', views.VendorProfile, name = 'VendorProfile'),
    path('menu-builder/', views.MenuBuilder, name = 'MenuBuilder'),
    path('menu-builder/category/<int:pk>/', views.FoodItemsByCategory, name='FoodItemsByCategory'),

    # Category CRUD
    path('menu-builder/category/create/', views.CreateCategory, name='CreateCategory'),
    path('menu-builder/category/update/<int:pk>/', views.UpdateCategory, name='UpdateCategory'),
    path('menu-builder/category/delete/<int:pk>/', views.DeleteCategory, name='DeleteCategory'),

    # food CRUD
    path('menu-builder/food/create/', views.CreateFood, name='CreateFood'),
    path('menu-builder/food/update/<int:pk>/', views.UpdateFood, name='UpdateFood'),
    path('menu-builder/food/delete/<int:pk>/', views.DeleteFood, name='DeleteFood'),
]