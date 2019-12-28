from django.db.models import Count
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from overflow.helper import FilterOption, pagination_limit
from overflow.models.QuestionModel import QuestionModel


def index(request):
    question_list = []
    current_page_number = 1

    if request.method == "GET":
        current_page_number = request.GET.get('page', 1)
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

    # adding pagination
    paginator = Paginator(question_list, pagination_limit())
    try:
        questions = paginator.page(current_page_number)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'overflow/index/index.html', {
        'questions': questions,
        'questions_count': question_list.count()
    })
