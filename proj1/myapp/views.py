from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User, Product # importing the classes defined in models.py of the app

# importing View to create a custom class-based view
from django.views import View

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