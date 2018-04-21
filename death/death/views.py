from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#return HttpResponse('hello wolid')
	return render(request,'index.html')

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def gallery(request):
	return render(request,'gallery.html')

def blog(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')

def gallerypost(request):
	return  render(request,'gallery-single-post.html')

def blogs(request):
	return render(request,'blog-single-post.html')
