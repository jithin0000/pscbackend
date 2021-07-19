from django.contrib import admin
from question.models import Question, Option
# Register your models here.
admin.site.register(Question)
admin.site.register(Option)
