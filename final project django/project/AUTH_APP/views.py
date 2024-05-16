from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup_view(request):
    template_name = 'AUTH_APP/signup.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    template_name = 'AUTH_APP/login.html'
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_orders_url')
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('login_url')