from django.core.exceptions import ValidationError
from django.views import generic
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserLogin


class ProfileView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user/user.html'


class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'user/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('user:login')

        return render(request, self.template_name, {'form' : form})


class UserLoginView(generic.View):
    form_class = UserLogin
    template_name = 'user/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('project:index')
            form.add_error('username', 'Invalid username or password')
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')
