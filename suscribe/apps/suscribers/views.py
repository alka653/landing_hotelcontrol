from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import *

def home(request, *args):
	title = 'Bienvenido'
	if request.method == 'POST':
		form = SuscriberForm(request.POST)
		if form.is_valid():
			if form.save():
				email = EmailMessage('Nuevo Registro', str('Nombre: '+request.POST['name']+'. Correo: '+request.POST['email']+'. Hotel: '+request.POST['hotel']), to = ['adriann.sanchez1@gmail.com', 'alka65@hotmail.com', 'laurentino-carranza@unipiloto.edu.co'])
				email.send()
				messages.add_message(request, 25, 'Exito en la inscripcion')
			else:
				messages.add_message(request, 40, 'Ha ocurrido un error')
			return HttpResponseRedirect('/')
	else:
		form = SuscriberForm()
	return render(request, 'home.html', {'title': title, 'form': form})