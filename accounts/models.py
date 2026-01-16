from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.db.models.fields.related import ForeignKey, OneToOneField


class User(AbstractBaseUser, PermissionsMixin):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE =(
       ( VENDOR, 'Vendor'),
       (CUSTOMER, 'Customer'),
    )
    email = models.EmailField(_('email address'),max_length=100, unique=True, blank=True, null=True)
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

    def __str__(self):
         return str(self.email or self.username or self.pk)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True, related_name = 'profile')
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

    class Meta:
        verbose_name_plural = 'User Profile'
    
    def __str__(self):
         return str(self.user.username)


    


        # def __str__(self):
        #  Return the linked user's username or email or fallback to id
        #  return str(self.user.username or self.user.email or self.pk)

