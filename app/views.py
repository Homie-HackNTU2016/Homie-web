from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_list_or_404

from userp.models import Products

# Create your views here.


def index(request):
    """Index view."""
    if request.method == 'GET':
        products = get_list_or_404(Products.objects.all())
    return render(request, 'index.html', {'products': products})


def product(request):
    if request.method == 'GET':
        return render(request, 'product_detail.html')