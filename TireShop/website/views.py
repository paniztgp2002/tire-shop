from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer
from .forms import SignupForm

# Create your views here.

def index(request):
    return render(request, 'website/index.html', {})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['phone_number'], password=data['password'], first_name="customer")
            user.save()
            customer = Customer(user=user, name=data['name'], phone_number=data['phone_number'])
            customer.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'website/signup.html', {'form': form})


def log_in(request):  # avoid shadowing django's "login" function
    return render(request, 'website/login.html', {})


def product_page(request):
    return render(request, 'website/product_page.html', {})        


def products(request):
    return render(request, 'website/products.html', {})            
