from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Sum


class QuestionModel(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = RichTextField(null=True)
    tag = models.CharField(max_length=120, null=True)
    views = models.PositiveIntegerField(default=0)
    final_answer_id = models.IntegerField(null=True)
    asked_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    asked_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __repr__(self):
        return f'{self.title}'

    def tag_split(self):
        if self.tag:
            return self.tag.split(',')

    def answer_count(self):
        return self.am_question.count()

    def get_vote_count(self):
        result = self.qvm_question.aggregate(Sum('vote'))['vote__sum']
        if result:
            return result
        else:
            return 0


class QuestionVoteModel(models.Model):
    question = models.ForeignKey(QuestionModel, null=True, on_delete=models.CASCADE, related_name='qvm_question')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='qvm_user')
    vote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
