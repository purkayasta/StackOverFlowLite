from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from overflow import helper
from overflow.models import QuestionModel, AnswerModel
from overflow.forms.NewAnswerForm import AnswerForm
from overflow.models.AnswerModel import AnswerVoteModel


@login_required
def record_answer(request, question_pk):
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_model = answer_form.save(commit=False)
            question_object = get_object_or_404(QuestionModel, pk=question_pk)
            answer_model.question = question_object
            answer_model.answer_by = request.user
            answer_model.save()
            return redirect('question_detail', question_pk)
    else:
        return redirect('question_detail', question_pk)


@login_required
def voting(request, pk, operation, question_pk):
    print(pk)
    answer_object = AnswerModel.objects.get(pk=pk)
    if answer_object:
        voting_object = AnswerVoteModel.objects.filter(user=request.user).filter(answer=pk).first()
        if not voting_object:
            # nothing found , creating new object
            new_answer = AnswerVoteModel(answer=answer_object, user=request.user)
            new_answer.vote = helper.get_voting(new_answer.vote, operation)
            new_answer.save()
        else:
            # found question vote object so update the value
            voting_object.vote = helper.get_voting(voting_object.vote, operation)
            voting_object.save()
    return redirect('question_detail', question_pk)


@login_required
def set_final_answer(request, q_pk, a_pk):
    answer_object = AnswerModel.objects.get(pk=a_pk)
    question_object = QuestionModel.objects.get(pk=q_pk)
    if question_object and answer_object:
        question_object.final_answer_id = a_pk
        question_object.save()

    return redirect('question_detail', q_pk)
