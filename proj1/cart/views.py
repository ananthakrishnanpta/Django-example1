from django.shortcuts import render

# Create your views here.


def cart_home(request):
    request.session['cart_id'] = 1
    request.session['user'] = request.user.username
    context = {

    }
    template = "cart/home.html"
    return render(request, template, context)
