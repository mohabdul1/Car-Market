from django import forms
from .models import Car ,Profile
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = Car
        fields = ['ad_description','car_model', 'mamsha', 'publish_on', 'picture', 'about','car_type','car_price']
        widgets = {
            'publish_on': forms.DateTimeInput(attrs={'type': 'date'})
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Full Name')
    email = forms.EmailField(required=True)
    body = forms.CharField(widget=forms.Textarea)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)    


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender']
