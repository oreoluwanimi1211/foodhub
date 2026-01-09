from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager





class User(AbstractBaseUser, PermissionsMixin):
    RESTAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICE =(
       ( RESTAURANT, 'Restaurant'),
       (CUSTOMER, 'Customer'),
    )
    email = models.EmailField(_('email address'),max_length=100, unique=True)
    username = models.CharField(_('username'), max_length=100, unique=True)
    first_name = models.CharField(_('first name'),max_length=100, blank=True)
    phone_no = models.CharField(_('phone number'), max_length=11, blank=True)
    last_name = models.CharField(_('last name'),max_length=100, blank=True)
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
    is_active = models.BooleanField(_('active'),default=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_superuser = models.BooleanField(_('superuser status'),default=False)
    role = models.PositiveSmallIntegerField(_('staff status'),choices=ROLE_CHOICE, blank=True, null=True)
    last_login = models.DateTimeField(_('last login'), auto_now_add=True)
    Created_date =models.DateTimeField(_('last login'), auto_now_add=True)
    modifield_date=models.DateTimeField(_('modifield date'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.email

                        

















































    
# class User(AbstractBaseUser, PermissionsMixin):
#     RESTAURANT = 1
#     CUSTOMER = 2

#     ROLE_CHOICE =(
#        ( RESTAURANT, 'Restaurant'),
#        (CUSTOMER, 'Customer'),
#     )
#     email = models.EmailField(_('email address'),max_length=100, unique=True)
#     username = models.CharField(_('username'), max_length=100, unique=True)
#     first_name = models.CharField(_('first name'),max_length=100, blank=True)
#     phone_no = models.CharField(_('phone number'), max_length=11, blank=True)
#     last_name = models.CharField(_('last name'),max_length=100, blank=True)
#     date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
#     is_active = models.BooleanField(_('active'),default=True)
#     is_staff = models.BooleanField(_('staff status'),default=False)
#     role = models.PositiveSmallIntegerField(_('role '),choices=ROLE_CHOICE, on_delete=models.CASCADE)
#     is_superuser = models.BooleanField(_('superuser status'),default=False)
#     role = models.CharField(_('staff status'),choices=ROLE_CHOICE, on_delete=models.CASCADE)
#     last_login = models.DateTimeField(_('last login'), auto_now_add=True)
#     Created_date =models.DateTimeField(_('last login'), auto_now_add=True)
#     modifield_date=models.DateTimeField(_('modifield date'), auto_now_add=True)


#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []