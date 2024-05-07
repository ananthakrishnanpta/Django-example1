from django.urls import path
from .views import HomeView, CreateProduct, ProductListing, ProductDetails, EditProduct, DeleteProduct
from . import views # importing views.py to import it's defined Http response functions

urlpatterns = [
    # path('', views.myapp, name='myapp'),
    # path('', HomeView.as_view(), name='myapp' ), # instead of using the FBV called 'myapp', we are using this CBV for homepage
    path('',ProductListing.as_view(),name='myapp'), # This is a generic CBV, replacing our previous versions of views for home.
    path('login', views.userLogin, name=''),
    # path('prod_details/<int:id>', views.prod_details, name="prod_details" ),
    path('products/<int:pk>', ProductDetails.as_view(), name="prod_details_view"),
    # utilizing <int:id> in the url pattern to ensure unique url pattern for each individual product's details page.
    # the path() function replaces the <int:id> with the id number of the particular product from database.
    path('addProduct', CreateProduct.as_view(),name="create_prod_view" ),
    # below implemented is the url for the update view
    path('editProduct/<int:pk>', EditProduct.as_view(), name="edit_product" ),
    # below implemented is the url for delete view 
    path('delProduct<int:pk>', DeleteProduct.as_view(), name = "del_product"),

    # for the search box
    path('search/', views.search, name='search'),

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