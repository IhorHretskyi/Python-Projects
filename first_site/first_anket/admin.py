from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Question, Answer, Anket


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    pass

@admin.register(Anket)
class QuestionAdmin(ModelAdmin):
    pass

@admin.register(Answer)
class QuestionAdmin(ModelAdmin):
    pass
