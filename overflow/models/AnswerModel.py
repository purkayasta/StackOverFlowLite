from django.contrib.auth.models import User
from django.db import models

from overflow.models.ReplyModel import ReplyModel


class AnswerModel(models.Model):
    answer = models.CharField(max_length=120)
    views = models.PositiveIntegerField(default=0)
    reply = models.ForeignKey(ReplyModel, null=True, on_delete=models.CASCADE, related_name='AnswerModel')
    answer_at = models.DateTimeField(auto_now=True)
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.answer}'
