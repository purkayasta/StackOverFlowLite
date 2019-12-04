from django.shortcuts import render, redirect, get_object_or_404

from overflow.forms.NewAnswerForm import AnswerForm
from overflow.forms.NewQuestionForm import NewQuestionForm
from overflow.models import QuestionModel, AnswerModel


def ask_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewQuestionForm()
    return render(request, 'overflow/question/create.html', {
        'form': form
    })


def question_detail(request, pk):
    questions = get_object_or_404(QuestionModel, pk=pk)
    questions.views += 1
    questions.save()

    question_answers = AnswerModel.objects.filter(question_id=pk)

    form = AnswerForm()
    return render(request, 'overflow/question/details.html', {
        'single_question': questions,
        'answers': question_answers,
        'form': form
    })


def voting(request, pk, operation):
    question_object = QuestionModel.objects.get(pk=pk)
    if question_object:
        if operation == 1:
            question_object.votes += 1
        elif operation == 0:
            question_object.votes -= 1
        else:
            pass
        question_object.save()
    return redirect('question_detail', pk)
