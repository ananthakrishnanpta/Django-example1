from django.shortcuts import redirect, render
# from .forms import RegisterationForm
# from django.contrib.auth.forms import AuthenticationForm # imported on 29th April 2024
# from django.contrib.auth import authenticate, login

# following are imported to make the CBVs work

from django.views import generic 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.



# def register_page(request):
#     form = RegisterationForm()
#     context = {
#         "title" : "Registration Page",
#         "form"  : form
#     }

#     if request.method == 'POST':
#         form = RegisterationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=True)
#             user.set_password(user.password)
#             user.save()
#             return redirect('/login')
#         else:
#             return render(request, "register.html", context )
        

#     return render(request, "register.html", context )


# def login_page(request):

#     form = AuthenticationForm() # Creating a form object from django's authentical form class'

#     if request.method == "POST":
#         username = request.POST.get('username')
#         password_ = request.POST.get('password')
#         user = authenticate(username, password_)

#         if user != None:
#             login(request, user)
#             return redirect('/')
        

#     context = {
#         "title" : "Login Page",
#         "form" : 'form'
#     }


#     return render(request, "login.html", context)




# The below code is the class based views implementation

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')