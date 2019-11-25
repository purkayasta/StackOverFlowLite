from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from overflow.models import QuestionModel


class AnswerModel(models.Model):
    answer = RichTextField(max_length=120)
    views = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(QuestionModel, null=True, on_delete=models.CASCADE, related_name='AnswerModel')
    answer_at = models.DateTimeField(auto_now=True)
    answer_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.answer}'
