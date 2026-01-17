from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, VendorRegistrationForm
from accounts.models import User, UserProfile
from django.contrib import messages, auth
from accounts.utils import DetectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


# restrict the Vendor for accessing the customer page
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

# restrict the customer for accessing the Vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied

def registeruser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'your are already logged in!')
        return redirect('CustomerDashboard')
    elif request.method == 'POST':
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

            # Send verification email
            send_verification_email(request, user)
            ##

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
    if request.user.is_authenticated:
        messages.warning(request, 'your are already logged in!')
        return redirect('VendorDashboard')
    elif request.method == 'POST':
        # store the data and create the user
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

            # Send verification email
            send_verification_email(request, user)
            ##

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



def activate(request, uidb64, token):     
        # Activate the user by setting the is_active status to True
        return



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'your are already logged in!')
        return redirect('dashboard')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('myaccount')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'you are logged out')
    return redirect('login')

@login_required(login_url = 'login')
def MyAccount(request):
    user = request.user
    redirectUrl = DetectUser(user)
    return redirect(redirectUrl)

@login_required(login_url = 'login')
@user_passes_test(check_role_customer)
def CustomerDashboard(request):
    return render(request, 'accounts/CustomerDashboard.html')

@login_required(login_url = 'login')
@user_passes_test(check_role_vendor)
def VendorDashboard(request):
    return render(request, 'accounts/VendorDashboard.html')