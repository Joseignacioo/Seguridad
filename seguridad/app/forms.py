from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellidos',
            'email',
            'fecha_nacimiento',
            'roles',
        ]

class CustomAuthenticationForm(AuthenticationForm):
    # Puedes personalizar el formulario si es necesario
    pass