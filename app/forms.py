from django import forms
from .models import Tarea,Proyecto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 



class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

        widgets = {
            "fecha":forms.SelectDateWidget()
         }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields =["nombre"]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email","password1","password2"]

    

