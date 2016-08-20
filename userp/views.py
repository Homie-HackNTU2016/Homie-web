"""Views for app."""
import json

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.core.serializers.json import DjangoJSONEncoder


from .models import UserProfile


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


def profiles(request, userid):
    """Operatoin for user profile."""
    if request.method == 'GET':
        userprofile = get_object_or_404(UserProfile, id=userid)
        products = list(userprofile.products_set.values())
        output = userprofile.__dict__
        output.pop('_state', None)
        output['products'] = products
        return HttpResponse(json.dumps(output, cls=DjangoJSONEncoder), content_type='application/json')
