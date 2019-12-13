from django import forms
from .models import Solicitud, Tema

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        #fields = ('tipo', 'descripcion_sol')
        fields = ['tipo', 'descripcion_sol']

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ('tipotema','descripcion_tema')