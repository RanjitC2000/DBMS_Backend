from django.conf.urls import url
from django.urls import reverse
from django.urls import path
from . import views

urlpatterns = [

    path('', views.login,name='login'),

]
