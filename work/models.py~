from django.db import models

# Create your models here.

class Student(models.Model):
	rollno=models.IntegerField(default=0)
	name=models.CharField(max_length=100)
	Class=models.IntegerField(default=0)
	teacher_name=models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name
		
#class Login(models.Model):
#	email=models.EmailField(max_length=70)
#	password=models.CharField(widget=PasswordInput())

