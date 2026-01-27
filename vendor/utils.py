from .models import Vendor
from menu.models import Category
from django.shortcuts import get_object_or_404

def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor

def get_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    return category