from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import VendorRegistrationForm, UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from django.contrib import messages
from accounts.views import check_role_vendor
from django.contrib.auth.decorators import login_required, user_passes_test


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
        # profile, created = UserProfile.objects.get_or_create(user=request.user)
        # vendor, created = Vendor.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(instance=profile)
        vendor_form = VendorRegistrationForm(instance=vendor)

    context = {
        # 'vendor': vendor,
        # 'profile': profile,
        'profile_form': profile_form,
        'vendor_form': vendor_form,
    }
    return render(request, 'vendor/VendorProfile.html', context)
