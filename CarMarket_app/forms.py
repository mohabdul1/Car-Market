from django import forms
from .models import Car

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
    body = forms.CharField(widget=forms.Textarea, help_text='write your message here')

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'ahmed':
            raise forms.ValidationError('ommm, sorry you cann\' send us message')

        return name