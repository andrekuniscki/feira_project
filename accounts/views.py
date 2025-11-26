from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from market.models import Item

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('market:home')
            else:
                messages.error(request, 'Credenciais inválidas.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('accounts:login')

@login_required(login_url='accounts:login')
def profile_view(request):
    user = request.user
    items_count = Item.objects.filter(owner=user).count()
    items_bought = Item.objects.filter(owner=user, bought=True).count()
    
    context = {
        'user': user,
        'items_count': items_count,
        'items_bought': items_bought,
    }
    return render(request, 'accounts/profile.html', context)
