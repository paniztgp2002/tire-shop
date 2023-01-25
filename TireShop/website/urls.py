from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('login/', views.log_in, name = 'login'),
        path('signup/', views.signup, name = 'signup'),
        path('product/', views.product, name = 'product'),
        path('products/', views.products, name = 'products'),
        path('seller/', views.seller, name = 'seller'),
        path('seller/dashboard', views.seller_dashboard, name = 'seller'),
        path('seller/products', views.seller_products, name = 'seller-products'),
        path('seller/addproduct', views.seller_addproduct, name = 'seller-addproduct'),
]
