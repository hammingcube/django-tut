from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, this is index view of polls app!")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
