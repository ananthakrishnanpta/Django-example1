from django.urls import path
from .views import HomeView
from . import views # importing views.py to import it's defined Http response functions

urlpatterns = [
    # path('', views.myapp, name='myapp'),
    path('', HomeView.as_view(), name='myapp' ),
    path('login', views.userLogin, name=''),
    path('prod_details/<int:id>', views.prod_details, name="prod_details" )
    # utilizing <int:id> in the url pattern to ensure unique url pattern for each individual product's details page.
    # the path() function replaces the <int:id> with the id number of the particular product from database.

]

"""
the urlpatterns to be available to the client must be set up here.

for eg; if you are developing the website www.google.com
and the url
www.google.com/gmail is to be available to the client,

path("gmail",views.gmail_page, name="gmail")

is added to the urls 
where gmail_page is a view defined in the views.py to handle requests for this particular url pattern.
"""