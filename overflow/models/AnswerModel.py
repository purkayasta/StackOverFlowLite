from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from overflow.models import QuestionModel


class AnswerModel(models.Model):
    answer = RichTextField(max_length=120)
    views = models.PositiveIntegerField(default=0)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(QuestionModel, null=True, on_delete=models.SET_NULL, related_name='am_question')
    answer_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    answer_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __repr__(self):
        return f'{self.answer}'

    def get_vote_count(self):
        result = self.avm_answer.aggregate(Sum('vote'))['vote__sum']
        if result:
            return result
        else:
            return 0


class AnswerVoteModel(models.Model):
    answer = models.ForeignKey(AnswerModel, null=True, on_delete=models.CASCADE, related_name='avm_answer')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='avm_user')
    vote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
