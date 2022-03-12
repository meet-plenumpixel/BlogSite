# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from users import forms as user_forms
from users import models as user_model
from users.multiview import MultiUpdateView


# Create your views here.


class UserRegisterView(CreateView):
  form_class = user_forms.UserRegisterForm
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  

class UserProfileUpdateView(MultiUpdateView):
  template_name = 'users/profile.html'
  success_url = reverse_lazy('profile')
  multi_model = [
    {
      'model': User,
      'fields': ['username', 'email'],
      'pk': 'request.user.pk',
      'form_prefix': 'u_'
    },
    {
      'model': user_model.ProfileModel,
      'fields': ['image'],
      'pk': 'request.user.profilemodel.pk',
      'form_prefix': 'p_'
    },
  ]


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
