from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


def add(request):
    return render(request, 'add.html')


def contact(request):
    return render(request,'contact.html')


def detailes(request):
    return render (request, 'details.html')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request, 'register.html')


def market(request):
    return render(request,'market.html')