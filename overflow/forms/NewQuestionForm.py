from django import forms

from overflow.models.QuestionModel import QuestionModel


class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        help_text='Be specific!',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'What do you want to ask?',
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        max_length=14000,
        required=True,
        help_text='**Maximum 4000 character is allowed',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Please explain your questions in details',
                'class': 'form-control'
            }
        )
    )
    tag = forms.CharField(
        max_length=120,
        required=True,
        help_text='comma separated text',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = QuestionModel
        fields = [
            'title',
            'description',
            'tag'
        ]
