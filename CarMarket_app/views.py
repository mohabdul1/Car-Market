from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import CarForm , ContactForm , LoginForm , UserForm, ProfileForm
from .models import Car
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            return HttpResponseRedirect(reverse('market'))

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
            return HttpResponseRedirect(reverse('contact'))
    data = { 
        'form': form
    }
    return render(request, 'contact.html', data)

def send_email(name, email, body):
    print('sending email done')

def detailes(request):
    return render (request, 'details.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request, 'user is not active')
            else:
                messages.error(request, 'invalid username of password')
    
    data = {
        'form': form}
    return render(request,'login.html', data)


def register(request):
    userForm = UserForm()
    profileForm = ProfileForm()

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('home'))

    data = { 'userForm': userForm, 'profileForm': profileForm}
    return render(request, 'register.html', data)



def market(request):
    Cars = Car.objects.all()
    data = {
        'Cars': Cars
     }
    return render(request,'market.html', data)
