from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=128)

    def __str__(self):
        return self.question_text

class Anket(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Answer(models.Model):
    anket = models.ForeignKey(Anket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    fields = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

