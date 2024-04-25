from django.urls import path

from .views import register_page


urlpatterns = [
    path('signup/',register_page, name="register")
]