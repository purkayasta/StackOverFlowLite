from django.urls import path, re_path, register_converter

from ..views import index, question, answer
from overflow.helper import NegativeIntConverter

register_converter(NegativeIntConverter, 'negative_or_positive')

urlpatterns = [
    path('', index.index, name='home'),
    path('questions/', index.index),
    path('questions/ask/', question.ask_question, name='ask_question'),
    re_path(r'question/(?P<pk>\d+)/$', question.question_detail, name='question_detail'),
    re_path(r'question/(?P<question_pk>\d+)/answer/$', answer.record_answer, name='record_answer'),
    path('question/<int:pk>/<negative_or_positive:operation>', question.voting, name='q_vote'),
    path('answer/<int:pk>/<negative_or_positive:operation>/<int:question_pk>/', answer.voting, name='a_vote'),
    path('right/<int:q_pk>/<int:a_pk>/', answer.set_final_answer, name='final_answer')
]
