from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question

def index(request):
	questions = Question.objects.all()
	qlist = [q.question_text for q in questions]
	response = ','.join(qlist)
	return HttpResponse(response)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
