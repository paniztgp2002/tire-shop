from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    balance = models.IntegerField(default=0)
    def last_address(self):
        latest = Cart.objects.filter(customer_id=self.user.id).exclude(paid=False)
        if latest:
            return latest.latest('address').address
        return ""
    def last_postcode(self):
        latest = Cart.objects.filter(customer_id=self.user.id).exclude(paid=False)
        if latest:
            return latest.latest('postcode').postcode
        return ""


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    balance = models.IntegerField(default=0)


class Cart(models.Model):
    customer_id = models.IntegerField()
    paid = models.BooleanField(default=False)
    datetime = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, default="")
    postcode = models.CharField(max_length=20, default="")
    def totalprice(self):
        total = 0
        for product_in_cart in  CartContainsProduct.objects.filter(cart_id=self.id):
            quantity = product_in_cart.quantity
            price = type_models[product_in_cart.type].objects.get(id=product_in_cart.product_id).price
            total += quantity * price
        return total


class CartContainsProduct(models.Model):
    quantity = models.IntegerField(default=1)
    type = models.CharField(max_length=4)
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    def name(self):
        return type_models[self.type].objects.get(id=self.product_id).name
    def price(self):
        return type_models[self.type].objects.get(id=self.product_id).price
    def totalprice(self):
        return type_models[self.type].objects.get(id=self.product_id).price * self.quantity




class Tire(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    seller_id = models.IntegerField()
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    layer = models.IntegerField()
    pattern = models.CharField(max_length=20)
    size = models.IntegerField()
    def img(self):
        return "tire"


class Tube(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    seller_id = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    layer = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    def img(self):
        return "tube"


class Rim(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    seller_id = models.IntegerField()
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    layer = models.IntegerField()
    size = models.IntegerField()
    def img(self):
        return "rim"


class Organization(models.Model):    
    name = models.CharField(max_length=50)


class Deal(models.Model):
    datetime = models.DateField(auto_now_add=False)
    seald = models.BooleanField()


class DealContainsProduct(models.Model):
    quantity = models.IntegerField(default=1)
    deal_id = models.IntegerField()
    product_id = models.IntegerField()


type_models = {"tire": Tire, "tube": Tube, "rim": Rim}
