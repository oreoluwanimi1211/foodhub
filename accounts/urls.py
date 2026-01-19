from django.urls import path
from . import views
from . import utils
urlpatterns=[
    path('registeruser/', views.registeruser, name='registeruser'),
    path('registervendor/', views.registervendor, name='registervendor'),

    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('myaccount', views.MyAccount, name='myaccount'),
    path('CustomerDashboard/', views.CustomerDashboard, name= 'CustomerDashboard'),
    path('VendorDashboard/', views.VendorDashboard, name= 'VendorDashboard'),

    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('resetpasswordvalidate/<uidb64>/<token>/', views.ResetPasswordValidate, name = 'ResetPasswordValidate'),
    path('forgotpassword/', views.ForgotPassword, name = 'ForgotPassword'),
    path('resetpassword/', views.ResetPassword, name = 'ResetPassword'),
]