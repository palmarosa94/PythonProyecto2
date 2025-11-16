from django import forms
from .models import Pagos
import re

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['nro_siniestro', 'nro_factura', 'fecha_factura', 'importe']
        widgets = {
            'nro_siniestro': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_factura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000-0000000000'}),
            'fecha_factura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'importe': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean_nro_factura(self):
        nro_factura = self.cleaned_data['nro_factura']
        pattern = r'^\d{3}-\d{10}$'
        if not re.match(pattern, nro_factura):
            raise forms.ValidationError("El número de factura debe tener el formato 000-0000000000.")
        return nro_factura
