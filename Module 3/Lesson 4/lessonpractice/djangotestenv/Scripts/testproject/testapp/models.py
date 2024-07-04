import string
import django
from django.db import models
import django.utils
import django.utils.timezone


class Question(models.Model):

    question_text = models.CharField(max_length=100)
    question_author = models.CharField(max_length = 100, default="Анонимно")
    question_date = models.DateTimeField("Время создания вопроса", default=django.utils.timezone.now)
    question_is_correct = models.BooleanField(default=False)

    def is_Question(self):
        return self.question_text.__contains__("?")
    def set_question_is_correct(self):
        question_is_correct = self.is_Question()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    # votes = models.PositiveIntegerField(default=0)
    votes = models.IntegerField(default=0)


class SuperQuestion(Question):
    question_level = models.PositiveIntegerField(default=1)

    def set_Super_Level(self, level):
        self.question_level = abs(level)
    pass