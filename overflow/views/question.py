from django.shortcuts import render, redirect
from overflow.forms.NewQuestionForm import NewQuestionForm


def ask_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewQuestionForm()
    return render(request, 'overflow/question/index.html', {
        'form': form
    })
