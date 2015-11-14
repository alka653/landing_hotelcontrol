from django.forms import *
from django import forms
from .models import *

class SuscriberForm(forms.ModelForm):
	class Meta:
		model = Suscriber
		fields = '__all__'
		widgets = {
			'name': TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre Completo'}),
			'email': EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Correo Electronico'}),
		}
		exclude = ('date',)