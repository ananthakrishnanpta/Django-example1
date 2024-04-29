from django.urls import path

from .views import register_page, login_page


urlpatterns = [
    path('signup/',register_page, name="register"),
    path('login', login_page, name="login")
]