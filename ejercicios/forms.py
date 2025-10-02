from django import forms
from .models import Ejercicio

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ['nombre', 'descripcion', 'categoria', 'nivel']
