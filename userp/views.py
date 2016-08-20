"""Views for app."""
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as _login, logout as _logout


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
