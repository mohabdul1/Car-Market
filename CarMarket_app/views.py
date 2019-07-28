from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import CarForm , ContactForm
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
            Car = form.save(commit=True)
            if 'picture' in request.FILES:
                Car.picture = request.FILES['picture']
            Car.save()            
            messages.success(request, 'your book have been added succesfully')
            return HttpResponseRedirect(reverse('add/'))

    data = {
        'form': form
    }
    return render(request, 'add.html',data)


def contact(request): 
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            send_email(name, email, body)
            form = ContactForm()
            messages.success(request, 'email is sent, we will contact you soon')
            return HttpResponseRedirect(reverse('contact.html'))
    data = { 
        'form': form
    }
    return render(request, 'contact.html', data)

def send_email(name, email, body):
    print('sending email done')

def detailes(request):
    return render (request, 'details.html')


def login(request):

    return render(request,'login.html')


def register(request):
    return render(request, 'register.html')


def market(request):
    return render(request,'market.html')
