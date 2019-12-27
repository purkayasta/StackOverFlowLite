from django.db.models import Count
from django.shortcuts import render

from overflow.helper import FilterOption
from overflow.models.QuestionModel import QuestionModel


def index(request):
    if request.method == "GET":
        question_filter = request.GET.get('query', None)
        if question_filter is None:
            question_list = QuestionModel.objects.all()
        else:
            if question_filter == FilterOption.all.name:
                question_list = QuestionModel.objects.all()
            elif question_filter == FilterOption.newest.name:
                question_list = QuestionModel.objects.order_by('-asked_at')
            elif question_filter == FilterOption.most_voted.name:
                question_list = QuestionModel.objects.annotate(qvm_question_count=Count("qvm_question")).order_by(
                    '-qvm_question_count')
    else:
        question_search = request.POST.get('search_bar')
        if question_search is not None:
            question_list = QuestionModel.objects.filter(title__icontains=question_search)

    return render(request, 'overflow/index/index.html', {
        'questions': question_list
    })
