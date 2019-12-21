from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import LoginViewModel
from django.views import View


# Function Based View

# def user_login(request):
#     error = ''
#     template = 'accounts/login/index.html'
#     if request.method == 'POST':
#         form = LoginViewModel(request.POST)
#         if form.is_valid():
#             request_user = form.cleaned_data
#             user_name = request_user['username']
#             user_password = request_user['password']
#             user_is_exist = User.objects.filter(username=user_name)
#             if user_is_exist:
#                 user = authenticate(request, username=user_name, password=user_password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('home')
#                 else:
#                     error = 'Authentication Failed! Try Again.'
#             else:
#                 error = 'No user found !'
#         else:
#             error = "Fill up the required information !"
#     else:
#         if request.user.is_authenticated:
#             return redirect('home')
#
#     return render(request, template, {
#         'error': error
#     })

# Class based View

class UserLogin(View):
    template_name = 'accounts/login/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            error = ''
            return render(request, self.template_name, {
                'error': error
            })

    def post(self, request):
        form = LoginViewModel(request.POST)
        if form.is_valid():
            request_user = form.cleaned_data
            user_name = request_user['username']
            user_password = request_user['password']
            user_is_exist = User.objects.filter(username=user_name)
            if user_is_exist:
                user = authenticate(request, username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    error = 'Authentication Failed! Try Again.'
            else:
                error = 'No user found !'
        else:
            error = "Fill up the required information !"
        return render(request, self.template_name, {
            'error': error
        })
