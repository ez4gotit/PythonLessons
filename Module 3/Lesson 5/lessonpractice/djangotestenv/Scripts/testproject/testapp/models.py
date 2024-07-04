import string
import django
from django.db import models
import django.utils
import django.utils.timezone

class User(models.Model):
    username = models.CharField( max_length = 20, unique=True)
    avatar = models.URLField(default="https://media1.tenor.com/m/E_peUuGvtZcAAAAC/shrek-go.gif")

class Question(models.Model):
    question_name = models.CharField(max_length=20, default="Вопрос")
    question_text = models.CharField(max_length=100)
    question_author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_date = models.DateTimeField("Время создания вопроса", default=django.utils.timezone.now)
    def is_Question(self):
        return self.question_text.__contains__("?")
    




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    # votes = models.PositiveIntegerField(default=0)
    votes = models.IntegerField(default=0)


class SuperQuestion(Question):
    question_level = models.PositiveIntegerField(default=1)
    pass


