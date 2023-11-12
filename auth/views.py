from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registerer successfully')
            return redirect('register-url')
    else:
        form = RegistrationForm
    return render(request, 'auth/register.html', context={"form": form})
