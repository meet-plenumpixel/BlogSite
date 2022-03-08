from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from users import forms as user_forms
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.


class UserRegisterView(CreateView):
  form_class = user_forms.UserRegisterForm
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')


class UserProfileView(UpdateView):
  template_name = 'users/profile.html'
  


class UserLoginView(auth_views.LoginView):
  template_name = 'users/login.html'
  next_page = reverse_lazy('profile')

class UserLogoutView(auth_views.LogoutView):
  template_name = 'users/logout.html'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'users/password_reset.html'

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
  template_name = 'users/password_reset_done.html'

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'users/password_reset_confirm.html'

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
  template_name = 'users/password_reset_complete.html'


























# class ProfileTemplateView(TemplateView):
#   template_name = 'users/profile_edit.html'

# class UserSignupView(CreateView):
#   form_class = UserRegisterForm
#   # success_url = reverse_lazy('login')
#   success_url = reverse_lazy('signin')
#   # fields = ['username', 'email', 'password1', 'password2']
#   template_name = 'registration/signup.html'

# class UserSigninView(SuccessMessageMixin, LoginView):
#   success_message = "You were successfully logged in"
#   # next_page = redirect('signout')
#   # print(dir(next_page))

# class UserSignoutView(SuccessMessageMixin, LogoutView):
#   success_message = "You were successfully logged out"
#   next_page = reverse_lazy('signin')
  