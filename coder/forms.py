from django import forms
from coder.models import Abogados
from coder.models import Peritos, Jurisdicciones

class AbogadosForm(forms.ModelForm):
    class Meta:
        model = Abogados
        fields = ["nombre", "apellido", "email","nro_abogado"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form.control'}),
            "apellido": forms.TextInput(attrs={'class': 'form.control'}),
            "email": forms.EmailInput(attrs={'class': 'form.control'}),
            "nro_legajo": forms.NumberInput(attrs={'class': 'form.control'})
        }
        
class PeritosForm(forms.ModelForm):
    class Meta:
        model = Peritos
        fields = ["nombre", "apellido", "email","nro_perito"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form.control'}),
            "apellido": forms.TextInput(attrs={'class': 'form.control'}),
            "email": forms.EmailInput(attrs={'class': 'form.control'}),
            "nro_legajo": forms.NumberInput(attrs={'class': 'form.control'})
        }
        
class JurisdiccionesForm(forms.ModelForm):
    class Meta:
        model = Jurisdicciones
        fields = ["localidad", "provincia", "codigo"]
        widgets = {
            "localidad": forms.TextInput(attrs={'class': 'form.control'}),
            "provincia": forms.TextInput(attrs={'class': 'form.control'}),
            "codigo": forms.NumberInput(attrs={'class': 'form.control'})
        }