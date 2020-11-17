from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



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
    user.Type = value['usertype']
    user.save()
    subject='ThankYou for signing up for the service by me!'
    message='Welcome to Rural Water Supply and Management Service! We will be in touch with you for new updates.'
    from_email=settings.EMAIL_HOST_USER
    to_list=[settings.EMAIL_HOST_USER]
    send_mail(subject,message,from_email,to_list,fail_silently=True)
    return render(request, 'registered.html')