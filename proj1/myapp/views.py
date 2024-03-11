from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Product

# Create your views here.
def myapp(request):
    myusers = User.objects.all().values() # creating a list of all 'User' objects
    myproducts = Product.objects.all().values()
    template = loader.get_template('index.html') # loading the template
    # return loader.get_template('index.html').render()
    context = {
        'userlist' : myusers,    # providing the context for the data to be given to the template
        'productlist' : myproducts
    }
    return HttpResponse(template.render(context, request)) # rendering the webpage from the template and sending it to the client

def prod_details(request, id):
    product = Product.objects.get(id = id) # select * from Product where id = <some_id_number>
    context = {
        'product' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))

def userLogin(request):
    return HttpResponse("Hi, the login page is yet to be built !!!")