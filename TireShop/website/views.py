from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html', {})
def login(request):
    return render(request, 'website/login.html', {})
def signup(request):
    return render(request, 'website/signup.html', {})        
def product_page(request):
<<<<<<< Updated upstream
    return render(request, 'website/product_page.html', {})        
=======
    return render(request, 'website/product-page.html', {})
def products(request):
    return render(request, 'website/products.html', {})            
>>>>>>> Stashed changes

