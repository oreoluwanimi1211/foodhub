from django.urls import path,include
from accounts import views as AccountView
from . import views
urlpatterns=[
    path('', AccountView.VendorDashboard, name = 'vendor'),
    path('profile/', views.VendorProfile, name = 'VendorProfile'),
]