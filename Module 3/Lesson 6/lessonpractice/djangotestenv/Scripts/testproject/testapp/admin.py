from django.contrib import admin

from .models import Question, Choice, SuperQuestion, User

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SuperQuestion)
admin.site.register(User)
