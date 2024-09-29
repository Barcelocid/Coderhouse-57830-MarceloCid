from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import RecetaDulce, RecetaSalada, RecetaBebida

# Formulario de Registro de Usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Formulario de Inicio de Sesión
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


# Formulario para ingresar una receta dulce
class RecetaDulceForm(forms.ModelForm):
    class Meta:
        model = RecetaDulce  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_persona', 'nombre_receta', 'descripcion', 'fecha_subida', 'edad']  # Campos que quieres incluir


class RecetaSaladaForm(forms.ModelForm):
    class Meta:
        model = RecetaSalada  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_persona', 'nombre_receta', 'descripcion', 'fecha_subida', 'edad']  # Campos que quieres incluir

class RecetaBebidaForm(forms.ModelForm):
    class Meta:
        model = RecetaBebida  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_persona', 'nombre_receta', 'descripcion', 'fecha_subida', 'edad']  # Campos que quieres incluir


class BuscarRecetaForm(forms.Form):
    query = forms.CharField(label='Buscar receta', max_length=100)