from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def fun(request):
    return render(request,'d.html',{'name':''})

def adding(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    re = n1+n2


    return render(request,'add.html',{'add':re})

