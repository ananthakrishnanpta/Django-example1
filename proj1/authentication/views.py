from django.shortcuts import redirect, render
from .forms import RegisterationForm
# Create your views here.


def register_page(request):
    form = RegisterationForm()
    context = {
        "title" : "Registration Page",
        "form"  : form
    }

    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request, "register.html", context )
        

    return render(request, "register.html", context )
