from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from love.models import *

# Create your views here.

def index(request):
	c = {}
	c.update(csrf(request))
	existCrush=None
	if request.POST:
		print 'post request'
		name=request.POST['name']
		branch=request.POST['branch']
		email=request.POST['email']
		cname=request.POST['cname']
		cbranch=request.POST['cbranch']
		print name,branch,email,cname,cbranch
		newCrush=Crush(name=name,branch=branch,email=email,cname=cname,cbranch=cbranch)
		newCrush.save()
		#find the crush 
		existCrush =  Crush.objects.filter(name=cname,branch=cbranch,cname=name,cbranch=branch)
	return render_to_response('index.html',{'crush':existCrush},context_instance=RequestContext(request))