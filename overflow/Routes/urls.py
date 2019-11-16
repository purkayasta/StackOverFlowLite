from django.urls import path, re_path
from ..Views import Index

urlpatterns = [
    path('', Index.index),
    path('questions/', Index.index)
]