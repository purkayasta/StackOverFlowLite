from django.urls import path, re_path
from ..views import Index, question

urlpatterns = [
    path('', Index.index, name='home'),
    path('questions/', Index.index),
    path('questions/ask/', question.ask_question, name='ask_question'),
    re_path(r'question/(?P<pk>\d+)/$', question.question_detail, name='question_detail')
]
