from django.shortcuts import render
from django.http import HttpResponse
from .models import Request,Project,Community,Notice,LargeScale,BigProject,SmallScale,Appointment
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
 
def status(request):
    flag = 1
    if request.method == 'POST':
        values = request.POST
        for i in range(len(Request.objects.all())):
            if (str(values['username']) == str(Request.objects.all()[i].username)) and (str(values['Project ID']) == str(Request.objects.all()[i].Project_ID)):
                messages.success(request, "The Current status of the Project is "+str(Request.objects.all()[i].RequestStatus))
                flag = 0
        if flag:
            messages.error(request, "Unable to find the project please Try Again")            
    #return HttpResponse('THis is the project request')
    return render(request,'home/requeststatus.html')
def apply(request):
    if request.method=='POST':
        value = request.POST
        project = Project()
        project.Project_Type = value['Project_Type']
        project.Project_Scale = value['Project_Scale']
        project.save()
        return render(request,'home/requestprocessing.html')
    return render(request,'home/request.html')
    
def healthscheme(request):
    return render(request,'home/HC.html')

def community(request):
    community_messages = Community.objects.all().order_by('-date')
    notices = Notice.objects.all()
    return render(request,'home/community.html',{'messages': community_messages,'notices':notices})

def community_detail(request,slug):
    message = Community.objects.get(slug = slug)
    return render(request,'home/community_detail.html',{'message':message})

def Commessage(request):
    if request.method == 'POST':
        value = request.POST
        ComMessage = Community()
        ComMessage.title = value['Title']
        ComMessage.slug = value['Slug']
        ComMessage.body = value['Body']
        ComMessage.save()
        return render(request,'home/messageprocessing.html')
    
    return render(request,'home/messages.html')

def notice(request,title):
    notice = Notice.objects.get(Title = title)
    return render(request,'home/Notice.html',{'notice':notice})

def bigProj(request):
    bigProj = LargeScale.objects.all()
    funds = BigProject.objects.all()
    return render(request,'home/BigProjects.html',{'largeProjs':bigProj,'funds':funds})

def smallProj(request):
    smallProj = SmallScale.objects.all()
    return render(request,'home/SmallProjects.html',{'smallProjs':smallProj})

def appoint(request):
    if request.method == 'POST':
        value = request.POST
        appointment = Appointment()
        appointment.username = value['username']
        appointment.Personnel_ID = value['personnel']
        appointment.TimeSlot = value['time']
        appointment.save()
        return render(request,'home/appointprocessing/html')  
    return render(request,'home/appoint.html')