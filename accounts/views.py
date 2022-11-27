from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
# Create your views here.


def register_view(request):
    context = {
        'reg': True
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data.copy()
            clean_data.pop('password_confirm')
            get_user_model().objects.create_user(**clean_data)
            return redirect("/")
        else:
            context['form'] = form
    return render(request, 'accounts/register.html', context)


def login_view(request):
    context = {
        'login': True
    }
    next = request.GET.get('next', None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            if user:
                login(request, user)
                if next is not None:
                    return redirect(next)
                return redirect("/")
            else:
                messages.error(
                    request, "username or password is incorrect", 'danger')
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")
