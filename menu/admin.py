from django.contrib import admin
from .models import Category, FoodItems
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'vendor', 'created_at', 'updated_at')
    search_fields = ('category_name','vendor__vendor_name')

class FoodItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('food_title',)}
    list_display = ('food_title', 'price', 'is_available', 'vendor', 'category', 'created_at', 'updated_at')
    search_fields = ('food_title', 'vendor__vendor_name','category__category_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItems, FoodItemsAdmin)