from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , Http404
from .forms import CarForm , ContactForm , LoginForm , UserForm, ProfileForm
from .models import Car
from django.contrib import messages
from django.urls import reverse ,reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import CarSerializer , UserSerializer 
from django.contrib.auth.models import User 


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





def home(request):
    return render(request,'home.html')
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'add.html'

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('home')
    template_name = 'car_delete.html'

def add(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Car = form.save(commit=False)
            Car.user = request.user
            if 'picture' in request.FILES:
                Car.picture = request.FILES['picture']
            Car.save()            
            messages.success(request, 'your car have been added succesfully')
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

def detailes(request, pk):
    car = Car.objects.filter(pk=pk).first()
    if car ==None:
        raise Http404()
    data = {
        'car' : car
    }
    return render (request, 'detailes.html', data)

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
