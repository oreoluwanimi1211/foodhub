from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import User


def registeruser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ROLE = User.CUSTOMER
            form.save()
            return redirect('registeruser')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registeruser.html', context)