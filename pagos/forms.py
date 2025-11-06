from django import forms
from .models import Pagos

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['importe', 'nro_siniestro']
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nro_siniestro': forms.TextInput(attrs={'class': 'form-control'}),
        }

