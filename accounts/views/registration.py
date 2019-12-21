from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


# def user_registration(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         if request.user.is_authenticated:
#             return redirect('home')
#         form = UserCreationForm()
#     return render(request, 'accounts/registration/index.html', {
#         'form': form
#     })


class UserRegistration(View):
    template_name = 'accounts/registration/index.html'
    form_class = UserCreationForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {
            'form': form
        })
