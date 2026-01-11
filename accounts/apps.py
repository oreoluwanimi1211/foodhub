from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


# def ready(self):
#     import accounts.signals    
#     " the code that make the signals to work"