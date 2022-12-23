from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, UploadForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/display_list')
            else:
                return redirect('/login')
        else:
                return redirect('/login')
    login_form = AuthenticationForm()
    return render(request, 'registration/login.html', {'login_form': login_form})

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            auth_login(request, user)
            return redirect('/display_list')
    else:
        register_form = RegisterForm()
    return render(request, 'sign_up.html', {'register_form': register_form})


@login_required(login_url='/login')
def upload(request):
    upload_form = UploadForm()
    return render(request, 'upload.html', {'upload_form': upload_form})


@login_required(login_url='/login')
def display_list(request):
    return render(request, 'display_list.html')


@login_required(login_url='/login')
def display_text(request):
    return render(request, 'display_text.html')

@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    return redirect('/index')
