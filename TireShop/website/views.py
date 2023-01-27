from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Customer, Seller, Tire, Tube, Rim, Cart, CartContainsProduct
from .forms import SignupForm, LoginForm, SearchForm, AddForm
from urllib.parse import quote_plus
from itertools import chain

# Create your views here.


type_models = {"tire": Tire, "tube": Tube, "rim": Rim}


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = quote_plus(data['name'])
            redirect_url = f'/products?name={name}'
            if data['type'] != "all":
                type = quote_plus(data['type'])
                redirect_url += f'&type={type}'
            if data['size'] != 0:
                size = quote_plus(str(data['size']))
                redirect_url += f'&sizeFrom={size}'
                redirect_url += f'&sizeTill={size}'
            if data['pattern'] != '0':
                pattern = quote_plus(str(data['pattern']))
                redirect_url += f'&pattern={pattern}'
            return HttpResponseRedirect(redirect_url)
    else:
        form = SearchForm()

    tires = Tire.objects.all().order_by('?')
    if len(tires) > 5:
        tires = tires[:5]
    tubes = Tube.objects.all().order_by('?')
    if len(tubes) > 5:
        tubes = tubes[:5]
    rims = Rim.objects.all().order_by('?')
    if len(rims) > 5:
        rims = rims[:5]
    products = chain(tires, tubes, rims)

    return render(request, 'website/index.html', {"form": form, "products": products})

def signup(request):
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            return HttpResponseRedirect('/customer/dashboard')
        return HttpResponseRedirect('/seller/dashboard')
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['phone_number'], password=data['password'], first_name=data['user_type'])
            user.save()
            if data['user_type'] == "customer":
                cart = Cart(customer_id=user.id)
                cart.save()
                sther = Customer(user=user, name=data['name'], phone_number=data['phone_number'])
            else:
                sther = Seller(user=user, name=data['name'], phone_number=data['phone_number'])
            sther.save()
            login(request, user)
            return HttpResponseRedirect(f'/{data["user_type"]}')
    else:
        form = SignupForm()
    return render(request, 'website/signup.html', {'form': form})


def log_in(request):  # to avoid shadowing django's "login" function
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            return HttpResponseRedirect('/customer/dashboard')
        return HttpResponseRedirect('/seller/dashboard')
    
    wrong_credentials = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['phone_number'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(f"/customer/dashboard/")
            else:
                wrong_credentials = True
    form = LoginForm()
    return render(request, 'website/login.html', {"form": form, "wrong_credentials": wrong_credentials})


def product(request, product_type, product_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    if product_type not in type_models:
        return HttpResponseNotFound("The product that you are looking for doesn't exist.")

    product = get_object_or_404(type_models[product_type], id=product_id)
    if request.method == "POST":
        if request.user.first_name == "customer":
            quantity = request.POST.get("quantity")
            if quantity.isdigit():
                quantity = int(quantity)
                if 1 <= quantity <= product.quantity:
                    cart = Cart.objects.filter(customer_id=request.user.id).filter(paid=False)[0]
                    ccp = CartContainsProduct(quantity=quantity, type=product_type, cart_id=cart.id, product_id=product.id)
                    ccp.save()
                    product.quantity -= quantity
                    product.save()
                    return HttpResponseRedirect("/customer/cart")
            return HttpResponseNotFound("invalid amount / out of stock")
        return HttpResponseNotFound("Sellers can't buy products.")
    seller = Seller.objects.get(user=User.objects.get(id=product.seller_id))
    products = type_models[product_type].objects.all()
    return render(request, 'website/product.html', {"product": product, "seller": seller.name, "products": products})


def products(request):
    if request.GET:
        filters = []
        for type_model in request.GET.getlist("type"):
            if type_model in type_models:
                filters.append(["type", ": " + type_model])
        if request.GET.get("pattern") and request.GET.get("pattern") != '0':
            filters.append(["pattern", ": " + request.GET.get("pattern")])
            search_results = [Tire.objects.filter(pattern=request.GET.get("pattern"))]
        elif request.GET.get("type") in type_models:
            search_results = []
            for type_model in request.GET.getlist("type"):
                search_results.append(type_models[type_model].objects.all())
        else:
            search_results = [Tire.objects.all(), Tube.objects.all(), Rim.objects.all()]
        if request.GET.get("name"):
            filters.append(["name", ": " + request.GET.get("name")])
            for i in range(len(search_results)):
                search_results[i] = search_results[i].filter(name__contains=request.GET.get("name"))
        if request.GET.get("sizeFrom") and request.GET.get("sizeTill"):
            if request.GET.get("sizeFrom") != '0' and request.GET.get("sizeTill") != '0':
                filters.append(["size", ": "+request.GET.get("sizeFrom")+"-"+request.GET.get("sizeTill")])
                for i in range(len(search_results)):
                    search_results[i] = search_results[i].filter(size__range=(request.GET.get("sizeFrom"), request.GET.get("sizeTill")))
        if request.GET.get("priceFrom") and request.GET.get("priceTill"):
            filters.append(["price", ": "+request.GET.get("priceFrom")+"-"+request.GET.get("priceTill")])
            for search_result in search_results:
                search_results[i] = search_result[i].filter(price__range=(request.GET.get("priceFrom"), request.GET.get("priceTill")))
        search_result = chain(*search_results)
        return render(request, 'website/products.html', {"products": search_result, "found_anything": bool(search_result), "searched": True, "filters": filters})
    tires = Tire.objects.all().reverse()[:3]
    tubes = Tube.objects.all().reverse()[:3]
    rims = Rim.objects.all().reverse()[:3]
    return render(request, 'website/products.html', {"searched": False, "tires": tires, "tubes": tubes, "rims": rims})


def seller(request):
    if request.user.is_authenticated:
        if request.user.first_name == "seller":
            return HttpResponseRedirect('/seller/dashboard')
        return HttpResponseRedirect('/customer/dashboard')
    return HttpResponseRedirect('/login')


def seller_dashboard(request):
    if request.user.is_authenticated:
        if request.user.first_name == "seller":
            seller = Seller.objects.get(user=request.user)
            paid_carts = Cart.objects.filter(paid=True).values_list('id')
            tires_in_carts = CartContainsProduct.objects.filter(type='tire').filter(cart_id__in=paid_carts).values_list('product_id')
            tubes_in_carts = CartContainsProduct.objects.filter(type='tube').filter(cart_id__in=paid_carts).values_list('product_id')
            rims_in_carts = CartContainsProduct.objects.filter(type='rim').filter(cart_id__in=paid_carts).values_list('product_id')
            best_selling_tires = Tire.objects.filter(id__in=tires_in_carts).filter(seller_id=request.user.id)
            best_selling_tubes = Tube.objects.filter(id__in=tubes_in_carts).filter(seller_id=request.user.id)
            best_selling_rims = Rim.objects.filter(id__in=rims_in_carts).filter(seller_id=request.user.id)
            best_sellings = list(chain(best_selling_tires, best_selling_tubes, best_selling_rims))
            if len(best_sellings) > 3:
                best_sellings = best_sellings[:3]
            return render(request, 'website/seller.dashboard.html', {'seller': seller, "best_sellings": best_sellings})
        return HttpResponseRedirect('/customer/dashboard')
    return HttpResponseRedirect('/login')


def seller_products(request):
    if request.user.is_authenticated:
        if request.user.first_name == "seller":
            tires = Tire.objects.filter(seller_id=request.user.id)
            tubes = Tube.objects.filter(seller_id=request.user.id)
            rims = Rim.objects.filter(seller_id=request.user.id)
            products = chain(tires, tubes, rims)
            seller = Seller.objects.get(user=request.user)
            return render(request, 'website/seller.products.html', {"products": products, "seller": seller})
        return HttpResponseRedirect('/customer/dashboard')
    return HttpResponseRedirect('/login')


def seller_addproduct(request):
    if not request.user.is_authenticated:
        HttpResponseRedirect('/login')
    if request.user.first_name != "seller":
        return HttpResponseRedirect('/customer/dashboard')
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            this_model = type_models[data['type']]
            if data['type'] != "tire":
                del data['pattern']
            del data['type']
            new_product = this_model(seller_id=request.user.id, **data)
            new_product.save()
            return HttpResponseRedirect('/seller/products')
    else:
        form = AddForm()
    seller = Seller.objects.get(user=request.user)
    return render(request, 'website/seller.addproduct.html', {'form': form, 'seller': seller})


def customer(request):
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            return HttpResponseRedirect('/customer/dashboard')
        return HttpResponseRedirect('/seller/dashboard')
    return HttpResponseRedirect('/login')


def customer_dashboard(request):
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            customer = Customer.objects.get(user=request.user)
            return render(request, 'website/customer.dashboard.html', {"customer": customer})
        return HttpResponseRedirect('/seller/dashboard')
    return HttpResponseRedirect('/login')


def customer_cart(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")
    if request.user.first_name != "customer":
        return HttpResponseRedirect('/seller/dashboard')
    cart = Cart.objects.filter(customer_id=request.user.id).exclude(paid=True)
    customer = Customer.objects.get(user=request.user)
    address = customer.last_address()
    postcode = customer.last_postcode()
    if not cart:
        return render(request, 'website/customer.cart.html', {"customer": customer, "address": address, "postcode": postcode})
    cart = cart[0]
    if request.method == "POST":
        address = request.POST.get("address")
        postcode = request.POST.get("postcode")
        if postcode.isdigit():
            postcode = int(postcode)
            if customer.balance >= cart.totalprice():
                customer.balance -= cart.totalprice()
                cart.paid = True
                cart.address = address
                cart.postcode = postcode
                new_cart = Cart(customer_id=request.user.id)
                customer.save()
                cart.save()
                new_cart.save()
                cart_products = CartContainsProduct.objects.filter(cart_id=cart.id)
                for product_cart in cart_products:
                    product = type_models[product_cart.type].objects.get(id=product_cart.product_id)
                    seller = Seller.objects.get(user=User.objects.get(id=product.seller_id))
                    seller.balance += product_cart.totalprice()
                    seller.save()
                return HttpResponseRedirect("/customer/dashboard")
            return HttpResponseNotFound("not enough balance")
        return HttpResponseNotFound("invalid postcode")
    ccp = CartContainsProduct.objects.filter(cart_id=cart.id)
    return render(request, 'website/customer.cart.html', {"customer": customer, "cart": cart, "ccp": ccp, "address": address, "postcode": postcode})


def customer_purchases(request):
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            return render(request, 'website/customer.purchases.html', {})
        return HttpResponseRedirect('/seller/dashboard')
    return HttpResponseRedirect('/login')


def increase_balance(request):
    if request.user.is_authenticated:
        if request.user.first_name == "customer":
            if request.method == "POST":
                amount = request.POST.get("amount")
                if amount.isdigit():
                    amount = int(amount)
                    if not (10000 <= amount <= 1000000):
                        return HttpResponseNotFound("not a valid amount")
                    customer = Customer.objects.get(user=request.user)
                    customer.balance += amount
                    customer.save()
                    return HttpResponseRedirect("/customer/dashboard")
    return HttpResponseNotFound("you have come to the wrong place")


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/login")
