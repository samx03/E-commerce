from django.contrib import admin
from django.urls import path
from .views.home import index, Items, ProductDetailView, about_us, contact_us
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut, handlerequest, CashOnDelivery
from .views.orders import OrderView
from.middlewares.auth import auth_middleware

urlpatterns = [
    path('', index),
    path('product', Items.as_view(), name='productpage'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('cashOnDelivery', CashOnDelivery.as_view(), name='COD'),
    path('handlerequest', handlerequest, name='HandleRequest'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('About-us', about_us),
    path('Contact-us', contact_us)
]
