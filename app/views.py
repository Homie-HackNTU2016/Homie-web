from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404

from userp.models import Products

# Create your views here.


def index(request):
    """Index view."""
    if request.method == 'GET':
        products = get_object_or_404(Products.objects.values())
    return render(request, 'index.html', {'products': products})
