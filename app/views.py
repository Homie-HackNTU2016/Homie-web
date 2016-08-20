from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_list_or_404, get_object_or_404
from userp.models import Products

# Create your views here.


def index(request):
    """Index view."""
    if request.method == 'GET':
        products = Products.objects.all()
        return render(request, 'index.html', {'products': products})


def product(request, pid):
    if request.method == 'GET':
        product = get_object_or_404(Products.objects.values(), id=pid)
        return render(request, 'product_detail.html', {'product': product})
