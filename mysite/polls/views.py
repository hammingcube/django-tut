from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import render

def index(request):
	questions = Question.objects.all()
	context = {'question_list': questions}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'question': question})
