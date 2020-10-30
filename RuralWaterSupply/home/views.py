from django.shortcuts import render
from django.http import HttpResponse
from .models import Request
# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
def status(request):
    #return HttpResponse('THis is the project request')
    return render(request,'home/request.html')
def apply(request):
    return HttpResponse('This is where you apply for project')

def healthscheme(request):
    return HttpResponse('These are the health schemes')
def community(request):
    return HttpResponse('This is the community')

def requestpost(request):
    #return HttpResponse('Your Request is being processed!')
    values=request.POST
    # requestone=Requests()
    # requestone['username']='temp'
    # requestone['Project_ID']=1#temporary
    # requestone['RequestStatus']='planned'
    # requestone.save()
    return render(request,'home/requestprocessing.html')
