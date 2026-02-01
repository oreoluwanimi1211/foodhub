from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import VendorRegistrationForm, UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from django.contrib import messages
from accounts.views import check_role_vendor
from django.contrib.auth.decorators import login_required, user_passes_test
from menu.models import Category, FoodItems
from .utils import get_food, get_vendor, get_category
from menu.forms import CreateCategoryForm, CreateFoodForm
from django.template.defaultfilters import slugify


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def VendorProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorRegistrationForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Settings updated')
            return redirect('VendorProfile')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        vendor_form = VendorRegistrationForm(instance=vendor)

    context = {
        # 'vendor': vendor,
        # 'profile': profile,
        'profile_form': profile_form,
        'vendor_form': vendor_form,
    }
    return render(request, 'vendor/VendorProfile.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def MenuBuilder(request):
    vendor = get_vendor(request)
    categories = Category.objects.filter(vendor=vendor).order_by('created_at')
    # categories = Category.objects.all()

    context={
        'categories': categories,
    }
    return render(request,'vendor/MenuBuilder.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def FoodItemsByCategory(request, pk=None):
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk=pk)
    fooditems = FoodItems.objects.filter(vendor=vendor, category=category)
    context ={
        'fooditems': fooditems,
        'category': category,
    }
    return render(request, 'vendor/FoodItemsByCategory.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def CreateCategory(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            #vendor = Vendor.objects.get(user=request.user)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('MenuBuilder')
        else:
            print(form.errors)

    else:
        form = CreateCategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'vendor/CreateCategory.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def UpdateCategory(request, pk=None):
    category = get_category(request, pk=pk)
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('MenuBuilder')
        else:
            print(form.errors)

    else:
        form = CreateCategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'vendor/UpdateCategory.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def DeleteCategory(request, pk=None):
    category = get_category(request, pk=pk)
    category.delete()
    messages.success(request, 'Category has been deleted successfully!')
    return redirect('MenuBuilder')


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def CreateFood(request):
    if request.method == 'POST':
        form = CreateFoodForm(request.POST, request.FILES)
        if form.is_valid():
            food_title = form.cleaned_data['food_title']
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(food_title)
            form.save()
            messages.success(request, 'Food Item added successfully!')
            return redirect('FoodItemsByCategory', food.category.id)
        else:
            print(form.errors)
    else:
        form = CreateFoodForm()
        #modify this form to return absolute category that belong to the particular vendor
        form.fields['category'].queryset = Category.objects.filter(vendor=get_vendor(request))
    context = {
        'form':form,
    }
    return render(request, 'vendor/CreateFood.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def UpdateFood(request, pk=None):
    food = get_food(request, pk=pk)
    if request.method == 'POST':
        form = CreateFoodForm(request.POST, instance=food)
        if form.is_valid():
            food_title = form.cleaned_data['food_title']
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(food_title)
            form.save()
            messages.success(request, 'Food item has been updated successfully')
            return redirect('FoodItemsByCategory', food.category.id)
        else:
            print(form.errors)
    else:
        form = CreateFoodForm(instance=food)
        #modify this form to return absolute category that belong to the particular vendor
        form.fields['category'].queryset = Category.objects.filter(vendor=get_vendor(request))
    context = {
        'form': form,
        'food': food,
    }
    return render(request, 'vendor/UpdateFood.html', context)


@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def DeleteFood(request, pk=None):
    food = get_food(request, pk=pk)
    food.delete()
    messages.success(request, 'Food has been deleted successfully!')
    return redirect('FoodItemsByCategory', food.category.id)