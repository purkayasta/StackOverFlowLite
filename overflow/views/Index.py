from django.shortcuts import render

from overflow.models.QuestionModel import QuestionModel


def index(request):
    question_list = QuestionModel.objects.all()
    return render(request, 'overflow/Index/index.html', {
        'questions': question_list
    })

