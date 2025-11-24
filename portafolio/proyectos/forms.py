from django import forms
from .models import Proyecto, Habilidad


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'experiencia', 'tipo', 'icono_url']
        widgets = {
            'experiencia': forms.NumberInput(attrs={'min': 0, 'max': 50}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'icono_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'})
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo',
            'descripcion',
            'imagen',
            'demo_url',
            'repo_url',
            'habilidades'
        ]
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'demo_url': forms.URLInput(attrs={'class': 'form-control'}),
            'repo_url': forms.URLInput(attrs={'class': 'form-control'})
        }