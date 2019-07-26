from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import CarForm
from .models import Car
from django.contrib import messages
from django.urls import reverse

def home(request):
    return render(request,'home.html')


def add(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Car = form.save(commit=False)
            if 'picture' in request.FILES:
                Car.picture = request.FILES['picture']
            Car.save()            
            messages.success(request, 'your book have been added succesfully')
            return HttpResponseRedirect(reverse('home'))

    data = {
        'form': form
    }
    return render(request, 'add.html',data)


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
