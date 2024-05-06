from django.urls import path
from .views import cart_home

app_name = "cart"

urlpatterns = [
    path('cartpage/', cart_home, name = "cartpage")
]