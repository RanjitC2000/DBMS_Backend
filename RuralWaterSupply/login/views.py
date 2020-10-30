from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from login.models import User


def login(request):
    return render(request, 'login/login.html')


def validate(request):
    values = request.POST
    users_list = []
    pass_list = []

    for i in range(len(User.objects.all())):
        users_list.append(User.objects.all()[i].username)
    j = 0
    for j in range(len(User.objects.all())):
        pass_list.append(User.objects.all()[j].password)
    # return HttpResponse(values['user'])
    j = 0
    
    if values['user'] in users_list:
        if values['password'] in pass_list:
            #return HttpResponse(' '.join(map(str,users_list )) + 'passwords'+ ' '.join(map(str,pass_list )))
            # return HttpResponse("this user is authorized!")
                
            return redirect('home')


    else:
        return render(request , 'login/error.html')
            #return render(request,'home/homepage.html')

