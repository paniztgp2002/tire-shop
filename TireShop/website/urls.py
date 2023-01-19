from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('login/', views.log_in, name = 'login'),
        path('signup/', views.signup, name = 'signup'),
        path('product_page/', views.product_page, name = 'product_page'),
        path('products/', views.products, name = 'products'),
]
