from django.urls import include, path
from django.shortcuts import redirect
from  . import views

urlpatterns = [

    # http://127.0.0.1:8000/testapp/
    path("", views.index, name = "index"),


    path("<int:question_id>/", views.question_details, name="question_details"),
        # http://127.0.0.1:8000/testapp/12312321/results/
    path("<int:question_id>/results/", views.question_results, name="question_results"),
    path("<int:question_id>/vote/", views.question_vote, name="question_vote"),

]