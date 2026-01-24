from django import forms
from .models import User, UserProfile
from vendor.models import Vendor
from .validators import allow_only_image_validator

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
    vendor_license= forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}), validators=[allow_only_image_validator])
    class Meta:
        model = Vendor
        fields = ('vendor_name','vendor_license')


class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'start typing....', 'required': 'required'}))
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}), validators=[allow_only_image_validator])
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}), validators=[allow_only_image_validator])


    # latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = UserProfile
        fields =['profile_picture','cover_photo', 'address', 'country','state','city','pin_code','latitude','longitude']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'latitude' or field == 'longitude':
                self.fields[field].widget.attrs['readonly'] = 'readonly'