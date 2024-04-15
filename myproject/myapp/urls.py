from django.urls import path , include
from .views import HomeView , product , add_to_cart , remove_from_cart ,ProductsView , OrderSummaryView ,Contact, remove_single_item_from_cart , CheckoutView , PaymentView , AddCouponView , contact_us , about_us
app_name = 'myapp'
urlpatterns = [
    path('', HomeView.as_view() , name = "home"),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path("checkout", CheckoutView.as_view() , name = "checkout"),
    
    path("product/<slug>/", product.as_view() , name = "product"),
    path("add-to-cart/<slug>/", add_to_cart , name = "add-to-cart"),
    path("remove-from-cart/<slug>/", remove_from_cart , name = "remove-from-cart"),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path("product/<slug>/", product.as_view() , name = "product"),
    path("aboutus/", about_us.as_view() , name = "aboutus"),
    path("allproducts/", ProductsView.as_view() , name = "allproducts"),
    path("contactus/", Contact , name = "contactus"),
]