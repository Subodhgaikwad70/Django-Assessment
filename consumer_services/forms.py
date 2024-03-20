# consumer_services/forms.py

from django import forms
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attached_file']

class TrackServiceForm(forms.Form):
    request_id = forms.IntegerField(label='Service Request ID')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')