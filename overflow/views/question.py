from django.shortcuts import render, redirect, get_object_or_404
from overflow.forms.NewQuestionForm import NewQuestionForm
from overflow.models import QuestionModel


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
    return render(request, 'overflow/question/details.html', {
        'single_question': questions
    })
