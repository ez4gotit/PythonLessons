import string
import django
from django.db import models
import django.utils
import django.utils.timezone
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_author = models.CharField(max_length = 100, default="Анонимно")
    question_date = models.DateTimeField("Время создания вопроса", default=django.utils.timezone.now)
    def is_Question(self):
        return self.question_text.__contains__("?")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    votes = models.IntegerField(default=0)