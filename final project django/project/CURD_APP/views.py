from django.shortcuts import render, redirect
from .forms import OrderForm
from django.http import HttpResponse
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_url')
def order_view(request):
    template_name = 'CURD_APP/order.html'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_orders_url')
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_view(request):
    tamplate_name = 'CURD_APP/show_orders.html'
    data = Order.objects.all()
    context = {'data': data}
    return render(request, tamplate_name, context)

@login_required(login_url='login_url')
def update_view(request, pk):
    obj = Order.objects.get(oid=pk)
    template_name = 'CURD_APP/Order.html'
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_orders_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def delete_view(request, pk):
    obj = Order.objects.get(oid=pk)
    template_name = 'CURD_APP/confirm.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('show_orders_url')
    return render(request, template_name)
