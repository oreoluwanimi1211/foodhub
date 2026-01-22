from django.shortcuts import render

def VendorProfile(request):
    return render(request, 'vendor/VendorProfile.html')
