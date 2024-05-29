from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form' : form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login')
    else:
        return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm})

    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('post:list')
    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('post:list')

def myblog(request):
    posts = request.user.posts.all().order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts' : posts})