from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Anket, Answer, Question


class IndexView(View):
    def get(self, request):
        questionnaires = Anket.objects.all()
        return render(request,
                      'index.html', {'quest': questionnaires})


class SignUpView(View):
    def get(self, request):
        return render(request,
                      'registration.html')

    def post(self, request):
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['email'],
                                            password=request.POST['password1'])
            login(request, user)
            return redirect('/')
        else:
            return render(request,
                      'registration.html', {'error': 'Passwords are not '
                                                     'equal'})

class DetailView(View):

    def get(self, request, pk):
        anket = Anket.objects.get(id=pk)
        return render(request, 'detail.html', {'anket': anket})

    def post(self, request, pk):
        anket = Anket.objects.get(id=pk)
        answer = Answer(user=request.user,
                        anket=anket)
        answer_dict = {}
        for d in list(request.POST)[1:]:
            q = Question.objects.get(id=d)
            answer_dict[q.question_text] = 'да'

        answer.fields = str(answer_dict)
        answer.save()

        return HttpResponse('OK')