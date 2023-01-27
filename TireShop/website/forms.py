from django import forms
from django.core.validators import RegexValidator, MinValueValidator


class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50, widget=forms.NumberInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    user_type = forms.CharField(max_length=8)
    phone_number.validators.append(RegexValidator(r'^(09|98)[0-9]+$'))


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=50, widget=forms.NumberInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class SearchForm(forms.Form):
    name = forms.CharField(max_length=50)
    type = forms.CharField(max_length=5)
    pattern = forms.CharField(max_length=50, required=False)
    size = forms.IntegerField(required=False)


class AddForm(forms.Form):
    type = forms.CharField(max_length=4)
    name = forms.CharField(max_length=50)
    brand = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    quantity = forms.IntegerField()
    price = forms.IntegerField()
    size = forms.IntegerField()
    layer = forms.IntegerField()
    pattern = forms.CharField(required=False)
    name.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "name"})
    brand.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "brand"})
    description.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "description"})
    size.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "size"})
    layer.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "layer"})
    pattern.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "pattern"})
    price.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "price"})
    quantity.widget.attrs.update({"class": "form-control bg-dark text-light", "placeholder": "quantity"})
    price.validators.append(MinValueValidator(1000))
    quantity.validators.append(MinValueValidator(1))
