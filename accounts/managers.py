from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password,  **extra_fields):

        if not email:
            raise ValueError('user must signup with correct email')
        email=self.normalize_email(email)
        user =self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must have is_superuser=True,")
        
        return self._create_user(email, password, **extra_fields)









































































































   
    
# class Usermanager(BaseUserManager):
#     def create_user(self, first_name, last_name, username, email, password):

#         if not email:
#             raise ValueError('user must have a valid email')
        
#         if not username:
#             raise ValueError('user must set an username')
        
#         user = self.model(
#             email=email.normalize_email(email),
#             username = username,
#             first_name = first_name,
#             last_name = last_name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, first_name, last_name, username, email, password):
#         user = self.create_user(
#             email = email.normalize_email(email),
#             username = username,
#             first_name = first_name,
#             last_name = last_name,
#         )
#         user.is_active = True
#         user. is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

