from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import *

def home(request, *args):
	title = 'Bienvenido'
	if request.method == 'POST':
		form = SuscriberForm(request.POST)
		if form.is_valid():
			if form.save():
				messages.add_message(request, 25, 'Exito en la inscripcion')
			else:
				messages.add_message(request, 40, 'Ha ocurrido un error')
			return HttpResponseRedirect('/')
	else:
		form = SuscriberForm()
	return render(request, 'home.html', {'title': title, 'form': form})