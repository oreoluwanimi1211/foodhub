from django.shortcuts import render


def vendorregistration(request):
    return response(request, 'accounts/registervendor.html')