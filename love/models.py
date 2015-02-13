from django.db import models

# Create your models here.

class Crush(models.Model):

	def __str__(self):
		return self.email

	name =  models.CharField(max_length=200)
	branch = models.CharField(max_length=10)
	cname = models.CharField(max_length=200)
	cbranch = models.CharField(max_length=10)
	email = models.CharField(max_length=100)
	#noteGenDate=models.DateTimeField('note date generated')