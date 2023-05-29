from itertools import product
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from .forms import  LoginForm
from django.http import Http404
from .forms import EditUserForm
from django.contrib.auth import login,authenticate,logout
from eshop_products.models import Product
from django.shortcuts import render, redirect
from eshop_accounts.models import User
from .forms import LoginForm, RegistrationForm      

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
    context = {
        'form': forms
    }
    return render(request, 'account/login.html', context)


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username,  email=email,password=password)
                    return redirect('/login')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'account/register.html', context)
    context = {
        'form': forms
    }
    return render(request, 'account/register.html', context)

def signout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='/login/')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None,
                                  initial={'first_name': user.first_name, 'last_name': user.last_name})

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {'edit_form': edit_user_form}

    return render(request, 'account/edit_account.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})



def favorite(request):
    new=request.user.fa_user.all()
    context={'new': new}
    return render(request,'account/fav.html',context)


def favorite_product(request, productId):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=productId)
    is_favorite = False
    if product.favorite.filter(id=request.user.id).exists():
       product.favorite.remove(request.user)
    else:
        product.favorite.add(request.user)
        is_favorite = True
    return redirect(url)


    




