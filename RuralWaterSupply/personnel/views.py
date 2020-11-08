from django.shortcuts import render
from django.http import HttpResponse
from home.models import Request,Project,Community,Notice
from django.contrib import messages

def home(request):
    return render(request,'personnel/homepage_local.html')

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
    return render(request,'personnel/requeststatus.html')

   
def publish(request):
    if request.method == 'POST':
       value = request.POST
       notices = Notice()
       notices.FirstName = value['fname']
       notices.LastName = value['lname']
       notices.Title = value['Title']
       notices.Body = value['Body']
       notices.save()
       messages.success(request, "Message Published!!")
    return render(request,'personnel/publish.html')

def healthscheme(request):
    return render(request,'personnel/HC.html')

def community(request):
    community_messages = Community.objects.all().order_by('date')
    notices = Notice.objects.all()
    return render(request,'personnel/community.html',{'messages': community_messages,'notices':notices})

def community_detail(request,slug):
    message = Community.objects.get(slug = slug)
    return render(request,'personnel/community_detail.html',{'message':message})

def Commessage(request):
    if request.method == 'POST':
        value = request.POST
        ComMessage = Community()
        ComMessage.title = value['Title']
        ComMessage.slug = value['Slug']
        ComMessage.body = value['Body']
        ComMessage.save()
        return render(request,'personnel/messageprocessing.html')
    
    return render(request,'personnel/messages.html')

def notice(request,title):
    notice = Notice.objects.get(Title = title)
    return render(request,'personnel/Notice.html',{'notice':notice})