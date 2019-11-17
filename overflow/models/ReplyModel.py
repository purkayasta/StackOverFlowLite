from django.contrib.auth.models import User
from django.db import models

from overflow.models.QuestionModel import QuestionModel


class ReplyModel(models.Model):
    reply = models.CharField(max_length=120)
    question = models.ForeignKey(QuestionModel, null=True, on_delete=models.CASCADE, related_name='ReplyModel')
    reply_at = models.DateTimeField(auto_now=True)
    reply_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.reply}'
