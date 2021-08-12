from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('henchmen', views.henchmen),
    path('lair', views.lair),
    path('guns', views.guns),
    path('pit_traps', views.pit_traps),
    path('product/<int:product_id>', views.product),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
    path('view_cart', views.view_cart),
    path('checkout', views.checkout),
    path('reg_login', views.reg_login),
    path('register', views.register),
    path('login', views.login),
    path('no_user', views.no_user),
    path('logout', views.logout),
    path('cart_destroy/<int:orderproduct_id>', views.cart_destroy),
    path('checkout_destroy/<int:orderproduct_id>', views.checkout_destroy)
]