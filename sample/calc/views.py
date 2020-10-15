from django.shortcuts import render

# Create your views here.

def home(response):
    return render(response,'home.html')

def add(response):
    val1= int(response.POST['num1'])
    val2= int(response.POST['num2'])
    
    result = val1 + val2
    return render(response,'add.html',{'result':result})