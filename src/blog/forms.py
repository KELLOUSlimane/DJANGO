from django.forms import ModelForm,  ValidationError
from . import models
from .models import Client
from django import forms

class ClientFroms(ModelForm) :
    class Meta :
        model  = Client
        fields = '__all__'
       