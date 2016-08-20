"""Url routing rules."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^profiles/(?P<userid>\d+)', views.profiles, name='profiles'),
    url(r'', views.user, name='user'),
]
