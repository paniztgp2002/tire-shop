from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('login/', views.log_in, name = 'login'),
        path('signup/', views.signup, name = 'signup'),
        path('product/<str:product_type>/<int:product_id>/', views.product, name = 'product'),
        path('products/', views.products, name = 'products'),
        path('seller/', views.seller, name = 'seller'),
        path('seller/dashboard/', views.seller_dashboard, name = 'seller-dashboard'),
        path('seller/products/', views.seller_products, name = 'seller-products'),
        path('seller/addproduct/', views.seller_addproduct, name = 'seller-addproduct'),
        path('customer/', views.customer, name = 'customer'),
        path('customer/dashboard/', views.customer_dashboard, name = 'customer-dashboard'),
        path('customer/cart/', views.customer_cart, name = 'customer-cart'),
        path('customer/purchases/', views.customer_purchases, name = 'customer-purchases'),
        path('increaseBalance/', views.increase_balance, name = 'increase-balance'),
        path('logout/', views.log_out, name = 'logout'),
]
