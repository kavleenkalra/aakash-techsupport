# Create your views here
from django.http import HttpResponse,HttpResponseRedirect
from work.models import Student
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from work.forms import PostForm


def index(request):
	return HttpResponse('<h2>This is index.html</h2>')

def student(request):
	context=RequestContext(request)
	students=Student.objects.all()
	context_dict={'students':students}
	return render_to_response("work/student.html",context_dict,context)
	
def submit_post(request):
	context=RequestContext(request)
	if request.POST:
		postform=PostForm(data=request.POST)
		if postform.is_valid():
			postform.save(commit=True)
			return HttpResponseRedirect('/work/student')
		else:
			print postform.errors
			
	else:
		postform=PostForm()
		print postform
		
	context_dict={'postform':postform}
	
	return render_to_response("work/submitpost.html",context_dict,context)

