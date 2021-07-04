from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password =raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()


    return render(request, 'registration/register.html', {'form':form})
    
    
    
def home(request):
    return render(request, 'index.html')