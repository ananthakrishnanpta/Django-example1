from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User, Product # importing the classes defined in models.py of the app

# importing View to create a custom class-based view
from django.views import View

# importing Generic Class-Based Views

from django.views.generic import CreateView, ListView, DetailView

# Create your views here.

# These are function-based views

# The following view 'myapp' has been again implemented using Class based views down below for demo purposes. The CBV is 'HomeView'

def myapp(request):
    myusers = User.objects.all().values() # creating a list of all 'User' objects
    myproducts = Product.objects.all().values() # fetching a list of all 'Products' from database
    template = loader.get_template('index.html') # loading the template
    # return loader.get_template('index.html').render()
    context = {
        'userlist' : myusers,    # providing the context for the data to be given to the template
        'productlist' : myproducts # the variable 'productlist' will now be available to be rendered in the template 'index.html'

    }
    
    return HttpResponse(template.render(context, request)) # rendering the webpage from the template and sending it to the client

def prod_details(request, id): # handling the Http request dependant on the 'id' value received from the url pattern requested by client.

    product = Product.objects.get(id = id) # select * from Product where id = <some_id_number>
    context = {
        'product' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))

# This view is not fully implemented; will be done later.
def userLogin(request):
    return HttpResponse("Hi, the login page is yet to be built !!!")

################################################################################################################

# These are class-based views...


# This is a CBV version of the FBV called 'myapp' defined above --->

class HomeView(View):
    myusers = User.objects.all().values() # creating a list of all 'User' objects
    myproducts = Product.objects.all().values() # fetching a list of all 'Products' from database
    template = loader.get_template('index.html') # loading the template
    context = {
            'userlist' : myusers,    # providing the context for the data to be given to the template
            'productlist' : myproducts # the variable 'productlist' will now be available to be rendered in the template 'index.html'
            }
    def get(self, request):
        # return loader.get_template('index.html').render()
        return HttpResponse(self.template.render(self.context, request)) # rendering the webpage from the template and sending it to the client


################################################################################################################

# Now we explore the use of Class Based Generic Views

# CRUD operations 

# 1. C    
# We are defining a View for creating a product item
    
class CreateProduct(CreateView):
    model = Product
    fields = ['name', 'price', 'pic']
    success_url = "/" # On successful submission of the form, user is redirected to home page

# 2. R
# List View and DetailView are 2 frequently used Generic CBVs in Django
    
class ProductListing(ListView):
    # model = Product
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    ordering = ['-id'] 
    # This is to order the products in desc order according to their pk


# DetailView is inherited and a product details view is built
    
class ProductDetails(DetailView):
    queryset = Product.objects.all()
    template_name = 'prod_details.html'

    def get_context_data(self, *args, **kwargs):
        context =  super(ProductDetails, self).get_context_data(*args,**kwargs)
        return context
