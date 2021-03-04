from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from eshop_products.models import Product
from .models import Favorite


# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    context = {
        'login_form': login_form
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'account/login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form,
    }
    return render(request, 'account/register.html', context)


def logout_page(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/login')
def favorite_page(request):
    user_favorites = Favorite.objects.values_list('favorite_product').filter(
        current_user_id__exact=request.user.id)
    page_obj = Product.objects.filter(pk__in=user_favorites)
    # print(user_favorites)
    context = {
        'page_obj': page_obj
    }

    return render(request, 'account/user_favorite_products.html', context)
