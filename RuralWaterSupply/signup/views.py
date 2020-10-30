from django.shortcuts import render
from django.http import HttpResponse
from login.models import User


# Create your views here.
def signup(request):
    return render(request, 'signup.html')


def register(request):
    value = request.POST
    user = User()
    user.username = value['username']
    user.password = value['password']
    # user.Village_ID = 1  # randomly assigning values now
    user.First_name = value['fname']
    user.Last_name = value['lname']
    user.date_of_birth = value['DOB']
    user.save()
    return render(request, 'registered.html')