from django.shortcuts import render, redirect
from cart.models import Product, Order

# Create your views here.
def home(request):
    products = Product.objects.all()
    if request.method == 'POST':
        return redirect('/')
    orders = Order.objects.all()
    return render(request, 'home.html', {'products':products, 'orders':orders})
