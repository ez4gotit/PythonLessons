from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader

def index(request):
    questions = Question.objects.all()
    output = loader.get_template('testapp/index.html')

    context = {
        "questions": questions,
    }
    return HttpResponse(output.render(context, request))

def question_details(request, question_id):

    question = Question.objects.get(id = question_id)
    output = loader.get_template('testapp/question.html')
    context = {
        'question' : question
    }
    return HttpResponse(output.render(context, request))


def question_results(request,question_id):
    return HttpResponse("Вот результат номер %s." % question_id)
def question_vote(request, question_id):
    return HttpResponse("Вот голосование номер %s." % question_id)