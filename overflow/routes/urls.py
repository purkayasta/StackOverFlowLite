from django.urls import path, re_path

from overflow.views.answer import record_answer
from ..views import Index, question

urlpatterns = [
    path('', Index.index, name='home'),
    path('questions/', Index.index),
    path('questions/ask/', question.ask_question, name='ask_question'),
    re_path(r'question/(?P<pk>\d+)/$', question.question_detail, name='question_detail'),
    re_path(r'question/(?P<question_pk>\d+)/answer/$', record_answer, name='record_answer'),
    path('question/<int:pk>/<int:operation>', question.voting, name='voting')
]
