from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, VendorRegistrationForm
from accounts.models import User, UserProfile
from django.contrib import messages


def registeruser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # create user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()
            # create user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()

            messages.error(request, 'your account has been register succesfully!')
            return redirect('registeruser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registeruser.html', context)


def registervendor(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        v_form = VendorRegistrationForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            #user_profile = userprofile.objects.get(user=user)
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request,'your account has been succesfully created')
            return redirect('registervendor')
        else:
            print('invalid form')
            print(form.errors)
    else:
          form = UserRegistrationForm()
          v_form = VendorRegistrationForm()
          
    context = {
        'form': form,
        'v_form': v_form,
    }
    return render(request, 'accounts/registervendor.html', context)
