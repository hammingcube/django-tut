from django.test import TestCase
from polls.models import Question

from django.core.urlresolvers import reverse


class QuestionViewTests(TestCase):
	def test_url_works(self):
		"""
		See if the response we get is correct
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
	def test_new_question_gets_added_to_the_question_list(self):
		q = Question.objects.create(question_text='But why?')
		response = self.client.get(reverse('polls:index'))
		qs = [q.question_text for q in response.context['question_list']]
		print qs
		self.assertEqual('But why?' in qs, True)

class QuestionMethodTests(TestCase):
	def test_question_with_empty_text(self):
		"""
		question_text should be non-empty for every
		Question object
		"""
		q = Question()
		self.assertEqual(len(q.question_text), 0)

