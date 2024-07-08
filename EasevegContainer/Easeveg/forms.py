# modulo para crear formularios personalizados
#Se usa formularios personalizados para escoger como se renderizan las plantillas HTML
from typing import Any 
from django import forms
from django.contrib.auth.models import User
#formulario de django para inicio de sesión básico
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#Case que hereda de AuthenticationForm, el formulario estándar de inicio de sesión de Django
class MyAuthenticationForm(AuthenticationForm):
    #Campo de entrada para nombre usuario 
    username = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={"placeholder":"username"}))
    #Campo para contraseña
    password = forms.CharField(
        label=("Password"),
        #Impide que se eliminen espacio en blanco en extremos de la ontraeña
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder":"password"}),
    )
#Clase que hereda del formulario estándar de Django para crear usuarios
class MyUserCreationForm(UserCreationForm):
    #Método que se sobreescribe para personalización del formulario
    def __init__(self, *args: Any, **kwargs: Any):
        #LLama al constructor de clase base con los argumentos que se le pasaron al contructor inicial
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Password comprobation'})
        
