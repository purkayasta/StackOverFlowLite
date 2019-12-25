from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from overflow import helper
from overflow.forms.NewAnswerForm import AnswerForm
from overflow.forms.NewQuestionForm import NewQuestionForm
from overflow.models import QuestionModel, AnswerModel, QuestionVoteModel


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_by = request.user
            question.save()
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


# def voting(request, pk, operation):
#     question_object = QuestionModel.objects.get(pk=pk)
#     if question_object:
#         if operation == 1:
#             question_object.votes += 1
#         elif operation == 0:
#             question_object.votes -= 1
#         else:
#             pass
#         question_object.save()
#     return redirect('question_detail', pk)


# 1. Get the question object
# 2. Search this question to Question Voting table and fetch this by login user
# 3. If found Then update the voting column by requested operation
# 4. If not found then create the object with the updated voting column value.
# 5.


@login_required
def voting(request, pk, operation):
    question_object = QuestionModel.objects.get(pk=pk)
    if question_object:
        voting_object = QuestionVoteModel.objects.filter(user=request.user).filter(question=pk).first()
        if not voting_object:
            # nothing found , creating new object
            new_question = QuestionVoteModel(question=question_object, user=request.user)
            new_question.vote = helper.get_voting(new_question.vote, operation)
            new_question.save()
        else:
            # found question vote object so update the value
            voting_object.vote = helper.get_voting(voting_object.vote, operation)
            voting_object.save()
    return redirect('question_detail', pk)
