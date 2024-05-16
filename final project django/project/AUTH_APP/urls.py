from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('sv/', signup_view, name='signup_url'),
    path('loginv/', login_view, name='login_url'),
    path('logoutv/', logout_view, name='logout_url')
]