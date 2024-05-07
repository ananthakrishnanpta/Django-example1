from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import  Product # importing the classes defined in models.py of the app

# importing View to create a custom class-based view
from django.views import View

# importing Generic Class-Based Views

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# importing url utilities to help with redirections

from django.urls import reverse, reverse_lazy

##############################################################################################
# importing the forms here

# from .forms import EditForm

##############################################################################################

# Create your views here.

# These are function-based views

# The following view 'myapp' has been again implemented using Class based views down below for demo purposes. The CBV is 'HomeView'

def myapp(request):
    myproducts = Product.objects.all().values() # fetching a list of all 'Products' from database
    template = loader.get_template('index.html') # loading the template
    # return loader.get_template('index.html').render()
    context = {   # providing the context for the data to be given to the template
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
    myproducts = Product.objects.all().values() # fetching a list of all 'Products' from database
    template = loader.get_template('index.html') # loading the template
    context = {   # providing the context for the data to be given to the template
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
    template_name = 'product_list.html' # if this is not set, by default, template will be looked inside
                        # <app_name>/<model_name>_<view_type>.html
    ordering = ['-id'] 
    # This is to order the products in desc order according to their pk


# DetailView is inherited and a product details view is built
    
class ProductDetails(DetailView):
    queryset = Product.objects.all() # Here, 
    # in case of the entire schema being required from a model, model  = <model-name> can be used as well instead of Queryset
    
    template_name = 'prod_details.html'

    def get_context_data(self, *args, **kwargs):
        context =  super(ProductDetails, self).get_context_data(*args,**kwargs)
        return context

# 3. U
# UpdateView is inherited
    
class EditProduct(UpdateView):
    model = Product
    fields = ['name', 'price', 'pic']
    template = 'editProduct.html'
    success_url = "/"

# 4. D
# DeleteView is inherited
    
class DeleteProduct(DeleteView):
    model = Product
    template_name = "delProduct.html"
    success_url = reverse_lazy('myapp')


def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) #| Product.objects.filter(description__icontains=query)
    # The above is equivalent to 'SELECT * FROM Product WHERE name LIKE "%<query>%" '
    template = 'search_results.html'
    context =  {
        'results': results,
        'query': query
          }
    return render(request, template, context) 