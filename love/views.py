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
	sendmail=False
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
		if 'Unknown' not in cbranch:
			existCrush =  Crush.objects.filter(name=cname,branch=cbranch,cname=name,cbranch=branch)
		else:
			existCrush=Crush.objects.filter(name=cname,branch=cbranch,cname=name)
		if existCrush:
			sendmail=True
			email1=email
			for i in existCrush:
				email2=i.email
			# send mail to both of them
			print "$$$$$$$$$$$$$$$$$$"
			to = email1
			send_mail("We found your crush", "%s likes you.\n So go ahead!\n" % (cname),"jssatlove@gmail.com",to.split(' '), fail_silently=False)
			to = email2
			send_mail("We found your crush", "%s likes you.\n So go ahead!\n" % (name)+"\n","jssatlove@gmail.com",to.split(' '), fail_silently=False)

	return render_to_response('index.html',{'crushexists':sendmail},context_instance=RequestContext(request))