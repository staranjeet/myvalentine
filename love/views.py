from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from love.models import *
from django.core.mail import send_mail

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
		sendmail=False
		existCrush =  Crush.objects.filter(name=cname,cname=name)
		if existCrush:
			sendmail=True
			email1=email
			for i in existCrush:
				email2=i.email
			# send mail to both of them
			print "$$$$$$$$$$$$$$$$$$"
			to = "deshrajdry@gmail.com"
			send_mail("We found your crush", "There is someone who loves you alot. "+"\n"+"So keep waiting."+"\n","loveatjss@gmail.com",to.split(' '), fail_silently=False)
	return render_to_response('index.html',{'crush':existCrush},context_instance=RequestContext(request))