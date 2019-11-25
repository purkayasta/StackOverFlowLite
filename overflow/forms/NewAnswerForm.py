from ckeditor.widgets import CKEditorWidget
from django import forms

from overflow.models import AnswerModel


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(
        max_length=14000,
        required=True,
        widget=CKEditorWidget(
            attrs={
                'placeholder': 'Please explain your questions in details',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = AnswerModel
        fields = ['answer', ]
