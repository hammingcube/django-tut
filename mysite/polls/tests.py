from django.test import TestCase
from polls.models import Question

class QuestionMethodTests(TestCase):
	def test_question_with_empty_text(self):
		"""
		question_text should be non-empty for every
		Question object
		"""
		q = Question()
		self.assertEqual(len(q.question_text), 0)

