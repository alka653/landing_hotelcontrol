from django.db import models
from datetime import datetime

class Suscriber(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	date = models.DateField(default = datetime.now)
	def __str__(self):
		return self.name