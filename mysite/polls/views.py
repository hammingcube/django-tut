from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
	questions = Question.objects.all()
	context = {'question_list': questions}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
