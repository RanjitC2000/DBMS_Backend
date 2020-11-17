from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

def home(request):
    return render(request,'personnel/homepage_local.html')

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
    return render(request,'personnel/requeststatus.html',{'form':form})

   
def publish(request):
    if request.method == 'POST':
        form = PublishForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Published!!")
    else:
        form = PublishForm()
    return render(request,'personnel/publish.html',{'form':form})

def healthscheme(request):
    return render(request,'personnel/HC.html')

def community(request):
    community_messages = Community.objects.all().order_by('-date')
    notices = Notice.objects.all()
    return render(request,'personnel/community.html',{'messages': community_messages,'notices':notices})

def community_detail(request,subject):
    message = Community.objects.get(subject = subject)
    return render(request,'personnel/community_detail.html',{'message':message})

def Commessage(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'personnel/messageprocessing.html')
    else:
        form = CommunityForm()
    return render(request,'personnel/messages.html',{'form':form})

def notice(request,title):
    notice = Notice.objects.get(Title = title)
    return render(request,'personnel/Notice.html',{'notice':notice})

def bigProj(request):
    bigProj = LargeScale.objects.all()
    funds = BigProject.objects.all()
    return render(request,'personnel/BigProjects.html',{'largeProjs':bigProj,'funds':funds})

def smallProj(request):
    smallProj = SmallScale.objects.all()
    return render(request,'personnel/SmallProjects.html',{'smallProjs':smallProj})

def appointview(request):
    appoint = Appointment.objects.all()
    return render(request,'personnel/appointview.html',{'appoints':appoint})

def personnel(request):
    personnel = LocalPersonnel.objects.all()
    return render(request,'personnel/LocalPersonnel.html',{'personnels':personnel})

def organization(request):
    organization = Organization.objects.all()
    contact = OrganizationContact.objects.all()
    return render(request,'personnel/Organizeers.html',{'organizations':organization,'contacts':contact})

def village(request):
    village = Village.objects.all()
    return render(request,'personnel/village.html',{'villages':village})
