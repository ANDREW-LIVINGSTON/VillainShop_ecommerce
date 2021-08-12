from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import bcrypt

from .models import *

def index(request):
    return render(request, 'base.html')

def henchmen(request):
    return render(request, 'henchmen.html')

def lair(request):
    return render(request, 'lair.html')

def guns(request):
    return render(request, 'guns.html')

def pit_traps(request):
    return render(request, 'pit_traps.html')

def product(request, product_id):
    context = {
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'product.html', context)

def add_to_cart(request, product_id):
    if 'user_id' not in request.session:
        return redirect('/no_user')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id']), 
        }
        product = Product.objects.get(id=product_id)
        OrderProduct.objects.create(
            user = User.objects.get(id=request.session['user_id']),
            product = product
        )
        return render(request, 'cart.html', context)

def view_cart(request):
    if 'user_id' not in request.session:
        return redirect('/no_user')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'orderproducts' :OrderProduct.objects.all()
        }
    return render( request, 'view_cart.html', context)
    
def checkout(request):
    if 'user_id' not in request.session:
        return redirect('/no_user')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'orderproducts' :OrderProduct.objects.all()
        }
    return render( request, 'checkout.html', context)


def reg_login(request):
    return render(request, 'reg_login.html')


def register(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'first_name':
                messages.error(request, value, extra_tags='first_name')
            if key == 'last_name':
                messages.error(request, value, extra_tags='last_name')
            if key == 'reg_email':
                messages.error(request, value, extra_tags='reg_email')
            if key == 'reg_password':
                messages.error(request, value, extra_tags='reg_password')
            if key == 'confirm_pw':
                messages.error(request, value, extra_tags='confirm_pw')
        return redirect('/reg_login')
    else:
        hashed_password = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt. gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['reg_email'],
            password = hashed_password
        )
        request.session['user_id'] = user.id
        return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'log_email' :
                messages.error(request, value, extra_tags='log_email')
            if key == 'log_password' :
                messages.error(request, value, extra_tags='log_password')
        return redirect('/reg_login')
    else:
        user_list = User.objects.filter(email=request.POST['log_email'])
        if len(user_list) == 0:
            messages.error(request, '*We could not find a user with that email address.*', extra_tags='log_email')
            return redirect('/reg_login')
        else:
            user = user_list[0]
            if bcrypt.checkpw(request.POST['log_password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/')
            else:
                messages.error(request, '*Your password was incorrect.*', extra_tags='log_password')
                return redirect('/reg_login')

def no_user(request):
    return render(request, 'no_user.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def cart_destroy(request, orderproduct_id):
    orderproduct = OrderProduct.objects.get(id=orderproduct_id)
    orderproduct.delete()
    return redirect('/view_cart')

def checkout_destroy(request, orderproduct_id):
    orderproduct = OrderProduct.objects.get(id=orderproduct_id)
    orderproduct.delete()
    return redirect('/checkout')
