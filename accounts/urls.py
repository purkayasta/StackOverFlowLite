from django.urls import path
from .views import registration, login

urlpatterns = [
    path('registration/', registration.UserRegistration.as_view(), name='signup'),
    path('login/', login.UserLogin.as_view(), name='login'),
]
