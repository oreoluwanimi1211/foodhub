from django import forms
from .models import User
from vendor.models import Vendor

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email','role', 'password']

    def clean(self):
        clean_data = super(UserRegistrationForm, self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                 'password does not match'
                )
            
class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('vendor_name','vendor_license')