from django.contrib import admin

from .models import Question, Choice, SuperQuestion

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SuperQuestion)
