from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    return render(request,'home/homepage.html')
 
def status(request):
    flag = 1
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            for i in range(len(Request.objects.all())):
                if (str(form.cleaned_data['username']) == str(Request.objects.all()[i].username)) and (str(form.cleaned_data['Project_ID']) == str(Request.objects.all()[i].Project_ID)):
                    messages.success(request, "The Current status of the Project is "+str(Request.objects.all()[i].RequestStatus))
                    flag = 0
            if flag:
                messages.error(request, "Unable to find the project please Try Again")
    else:
        form = StatusForm()          
    return render(request,'home/requeststatus.html',{'form':form})

def apply(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/requestprocessing.html')
    else:
        form = ProjectForm()
    return render(request,'home/request.html',{'form':form})
    
def healthscheme(request):
    return render(request,'home/HC.html')

def community(request):
    community_messages = Community.objects.all().order_by('-date')
    notices = Notice.objects.all()
    return render(request,'home/community.html',{'messages': community_messages,'notices':notices})

def community_detail(request,subject):
    message = Community.objects.get(subject = subject)
    return render(request,'home/community_detail.html',{'message':message})

def Commessage(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'home/messageprocessing.html')
    else:
        form = CommunityForm()
    return render(request,'home/messages.html',{'form':form})

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
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/appointprocessing.html')
    else:
        form = AppointmentForm()
    return render(request,'home/Appointments.html',{'form':form})

def appointview(request):
    appoint = Appointment.objects.all()
    return render(request,'home/appointview.html',{'appoints':appoint})

def personnel(request):
    personnel = LocalPersonnel.objects.all()
    return render(request,'home/LocalPersonnel.html',{'personnels':personnel})

def organization(request):
    organization = Organization.objects.all()
    contact = OrganizationContact.objects.all()
    return render(request,'home/Organizeers.html',{'organizations':organization,'contacts':contact})

def village(request):
    village = Village.objects.all()
    return render(request,'home/village.html',{'villages':village})
