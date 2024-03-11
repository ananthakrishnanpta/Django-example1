from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('login', views.userLogin, name=''),
    path('prod_details/<int:id>', views.prod_details, name="prod_details" )
]