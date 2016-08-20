"""Views for app."""
import json
from datetime import datetime

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Products


def login(request):
    """Login view."""
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':

        response = 0
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user:
            _login(request, user)
            response = 1
        return HttpResponse(response)


def logout(request):
    """Logout view."""
    _logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profiles(request, userid):
    """Operatoin for user profile."""
    if request.method == 'GET':
        user = get_object_or_404(User, id=userid)
        products = list(user.userprofile.products_set.values())
        output = user.userprofile.__dict__
        output = {k: v for k, v in output.iteritems() if not k.startswith('_')}
        output['products'] = products
        return HttpResponse(
            json.dumps(
                output,
                indent=4,
                sort_keys=True,
                default=lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, datetime) else x,
            ),
            content_type='application/json'
        )


@login_required
def products(request):
    """Operation for products."""
    q = request.GET.get('q')

    if q:
        output = Products.objects.all().filter(name__contains=q)
        output = [{k: v for k, v in i.__dict__.iteritems() if not k.startswith('_')} for i in output]
    else:
        output = []
    return HttpResponse(
        json.dumps(
            output,
            indent=4,
            sort_keys=True,
            default=lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if isinstance(x, datetime) else x,
        ),
        content_type='application/json'
    )



def user(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            userprofile = get_object_or_404(User, id=request.user.id)
            products = list(userprofile.products_set.values())
            return render(request, 'profile.html', {'userProfile': userprofile, 'products': products})
        else:
            return render(request, 'login.html')

