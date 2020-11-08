from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login,logout

# Create your views here.
from login.models import User


def login(request):
    if request.method == 'POST':
        values = request.POST
        flag = 1
        for i in range(len(User.objects.all())):
            if(str(values['user']) == str(User.objects.all()[i].username) and str(values['password']) == str(User.objects.all()[i].password)):               
                flag = 0
                if(str(User.objects.all()[i].Type) == ' local personnel'):
                    return render(request,'personnel/homepage_local.html',{'user_name':values['user']})
                return render(request,'home/homepage.html',{'user_name':values['user']})
        
        if flag:
            return render(request , 'login/error.html')
    else:
        return render(request, 'login/login.html')


"""def validate(request):
    if request.method == 'POST':
        values = request.POST
        flag = 1
        for i in range(len(User.objects.all())):
            if(str(values['user']) == str(User.objects.all()[i].username) and str(values['password']) == str(User.objects.all()[i].password)):               
                flag = 0
                if(str(User.objects.all()[i].Type) == 'local personnel'):
                    return render(request,'home/homepage_local.html',{'user_name':values['user']})
                return render(request,'home/homepage.html',{'user_name':values['user']})
        
        if flag:
            return render(request , 'login/error.html')
    else:
        return render(request , 'login/.html')

            #return render(request,'home/homepage.html')"""