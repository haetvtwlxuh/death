from django.shortcuts import render
from lang.models import DeathLang
from lang.models import Langlist,LangText
from django.http import Http404

langs=Langlist.objects.all()


def index(request):
	n=DeathLang.objects.order_by('-date')[0].title
	lang=n.split(',')
	x=1
	return render(request,'index.html',{'lang':lang,'x':x})

def about(request):
	return render(request,'about.html')

def gallery(request):
	size=range(len(langs))
	images=['images/in-the-country.jpg','images/mustache2.jpg','images/mustache3.jpg','images/mustache4','images/mustache5','images/mustache6.jpg','images/mustache7.jpg']
	return render(request,'gallery.html',{'langlist':langs,'images':images[1],'size':size})

def blog(request,lang):
	for x in langs:
		if lang == x.name:
			langtext=x.langtext_set.all()
			return render(request,'blog.html',{'langtext':langtext})
		else:
			pass
	raise Http404('no is'+lang)

def contact(request):
	lang=DeathLang.objects.order_by('-date')
	return render(request,'contact.html',{'lang':lang})

def blogs(request):
	return render(request,'blog-single-post.html')

def error404(request):
	return render(request,'404.html')
