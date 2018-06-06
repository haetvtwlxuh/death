from django.shortcuts import render
from lang.models import DeathLang
from lang.models import Langlist,LangText
from django.http import Http404

langs=Langlist.objects.all()


def index(request):
	return render(request,'home.html')

def error404(request):
	return render(request,'404.html')
