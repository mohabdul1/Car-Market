from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = Car
        fields = ['car_model', 'mamsha', 'publish_on', 'picture', 'about','car_type','car_price']
        widgets = {
            'publish_on': forms.DateTimeInput(attrs={'type': 'date'})
        }