from django.urls import path

# importing the FBVs for authentication
# from .views import register_page, login_page

# importing the CBVs for authentication

from .views import UserRegisterView


urlpatterns = [
    # path('signup/',register_page, name="register"),
    path('signup/',UserRegisterView.as_view(), name='register'),
    # path('login', login_page, name="login")
]