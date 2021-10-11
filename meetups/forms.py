from django import forms
from django.forms import fields
from .models import Participant

# Model form way

# class RegistrationForm(forms.ModelForm):
    
#     class Meta:
#         model = Participant
#         fields = ['email', 'name']


# Dynamic Form way
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')