from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_list_or_404, get_object_or_404
from userp.models import Products, User

# Create your views here.


def index(request):
    """Index view."""
    if request.method == 'GET':
        products = Products.objects.all()
        return render(request, 'index.html', {'products': products})


def product(request, pid):
    if request.method == 'GET':
        product = get_object_or_404(Products, id=pid)
        owner = {
            'id': product.user.id,
            'username': product.user.user.username,
            'avatar': product.user.avatar,
        }
        print('---------------')
        print(product.user.avatar)
        print('---------------')
        return render(request, 'product_detail.html', {'product': product.__dict__, 'owner': owner})
