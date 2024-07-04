
from . import views
from django.urls import path
urlpatterns = [
    path('homepage1/', views.homepage , name='homepeage')
]