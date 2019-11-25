from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models


class QuestionModel(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = RichTextField(null=True)
    tag = models.CharField(max_length=120, null=True)
    views = models.PositiveIntegerField(default=0)
    asked_at = models.DateTimeField(auto_now=True)
    asked_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return f'{self.title}'

    def tag_split(self):
        if self.tag:
            return self.tag.split(',')

