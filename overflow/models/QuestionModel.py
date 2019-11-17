from django.contrib.auth.models import User
from django.db import models


class QuestionModel(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=120)
    views = models.PositiveIntegerField(default=0)
    asked_at = models.DateTimeField(auto_now=True)
    asked_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.title}'
