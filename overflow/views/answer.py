from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from overflow.models import AnswerModel, QuestionModel
from overflow.forms.NewAnswerForm import AnswerForm


def record_answer(request, question_pk):
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_model = answer_form.save(commit=False)
            question_object = get_object_or_404(QuestionModel, pk=question_pk)
            answer_model.question = question_object
            answer_model.answer_by = None
            answer_model.save()
            return redirect('question_detail')
    else:
        return reverse('question_detail', kwargs=('pk', question_pk))
