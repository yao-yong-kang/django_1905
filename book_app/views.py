from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('login')

def reg(request):
    return HttpResponse('regis')

def add(request):
    return HttpResponse('增加功能')