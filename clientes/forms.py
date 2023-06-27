from datetime import date
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'nit_cc', 'email', 'direccion', 'telefono', 'pago', 'fecha')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'pago': forms.NumberInput(attrs={'min': '0'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'})
        }
        labels = {
            'nit_cc': 'NIT/CC',
            'pago': 'Monto del pago'
        }

    def clean_nit_cc(self):
        nit_cc = self.cleaned_data['nit_cc']
        if Cliente.objects.filter(nit_cc=nit_cc).exists():
            raise forms.ValidationError('Este NIT/CC ya está registrado.')
        return nit_cc

    def clean_pago(self):
        pago = self.cleaned_data['pago']
        if pago <= 0:
            raise forms.ValidationError('El monto del pago debe ser positivo.')
        return pago

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha > date.today():
            raise forms.ValidationError('La fecha del pago no puede ser futura.')
        return fecha
