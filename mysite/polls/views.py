from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext, loader

def index(request):
	questions = Question.objects.all()
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'question_list' : questions,
	})
	return HttpResponse(template.render(context))
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
