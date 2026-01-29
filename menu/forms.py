from django import forms
from .models import Category, FoodItems
from accounts.validators import allow_only_image_validator


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class CreateFoodForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}), validators=[allow_only_image_validator])
    class Meta:
        model = FoodItems
        fields = ['category','food_title','image','description','price','is_available']