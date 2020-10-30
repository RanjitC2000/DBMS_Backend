from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register , name='register'),
    path('', views.signup, name='signup'),



]
