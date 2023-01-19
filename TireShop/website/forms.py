from django import forms


class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

