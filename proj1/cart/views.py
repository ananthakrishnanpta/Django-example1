from django.shortcuts import render
from .models import Cart
# Create your views here.


def cart_home(request):
    request.session['cart_id'] = 1
    request.session['user'] = request.user.username
    context = {

    }
    template = "cart/home.html"
    return render(request, template, context)


def update_cart(request):
    p = request.POST.get('price')
    q = request.POST.get('qnt')
    print(request.POST)
    id = request.POST.get('cid')
    totalprice = float(p) * int(q)
    Cart.objects.filter(id = id).update(quantity = q, totalprice = totalprice)
    total = Cart.objects.filter(user = request.user).aggregate(Sum('totalprice'))
    print(total)

    totalamount = total['totalprice_sum']
    Cart.amount = totalamount

    return JsonResponse({'status' : True, 'totalprice':totalprice, 'totalam' : Cart.amount })

