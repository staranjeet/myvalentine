from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from love.models import *

# Create your views here.

def index(request):
	c = {}
	c.update(csrf(request))
	if request.POST:
		print 'post request'
		name=request.POST['name']
		branch=request.POST['branch']
		email=request.POST['email']
		cname=request.POST['cname']
		cbranch=request.POST['cbranch']
		print name,branch,email,cname,cbranch
	return render_to_response('index.html',context_instance=RequestContext(request))