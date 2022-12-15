from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Sign In successfull!')
            return redirect('index')
        messages.error(request, 'Invalid Information, Please try again!')
    form = NewUserForm
    return render(request, 'signin.html', context={'form':form})

def user(request):
    user = request.user
    context = {
        'user' : user
    }

    return render(request, 'user.html', context)