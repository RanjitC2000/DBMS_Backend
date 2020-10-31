from django.shortcuts import render
from django.http import HttpResponse
from .models import Request,Project,Community

# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
def status(request):
    #return HttpResponse('THis is the project request')
    return render(request,'home/request.html')
def apply(request):
    return render(request,'home/request.html')
def healthscheme(request):
    return HttpResponse('These are the health schemes')
def community(request):
    community_messages = Community.objects.all().order_by('date')
    return render(request,'home/community.html',{'messages': community_messages})

def requestpost(request):
    #return HttpResponse('Your Request is being processed!')
    values=request.POST
    # requestone=Requests()
    # requestone['username']='temp'
    # requestone['Project_ID']=1#temporary
    # requestone['RequestStatus']='planned'
    # requestone.save()
    return render(request,'home/requestprocessing.html')

def save(request):
    if request.POST:
        value = request.POST
        project = Project()
        project.Project_Type = value['Project_Type']
        project.Project_Scale = value['Project_Scale']
        project.save()
        return render(request,'home/requestprocessing.html')
    else:
        return render(request,'home/requestprocessingerror.html')

def community_detail(request,slug):
    message = Community.objects.get(slug = slug)
    return render(request,'home/community_detail.html',{'message':message})

def Commessage(request):
    return render(request,'home/messages.html')

def SendMessage(request):
    if request.POST:
        value = request.POST
        ComMessage = Community()
        ComMessage.title = value['Title']
        ComMessage.slug = value['Slug']
        ComMessage.body = value['Body']
        ComMessage.save()
        return render(request,'home/messageprocessing.html')
    