from django.test import TestCase
from .models import Question, Choice
from django.test import TestCase
from django.utils import timezone
import datetime


# Create your tests here.


class QuestionMethodTests(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
