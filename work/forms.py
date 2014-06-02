from django import forms
from models import Student

class PostForm(forms.ModelForm):
	
	rollno=forms.IntegerField()
	name=forms.CharField(max_length=100)
	Class=forms.IntegerField()
	teacher_name=forms.CharField(max_length=100)
	
	
	class Meta:
		model=Student
		fields=['rollno','name','Class','teacher_name']
