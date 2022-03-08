from django.urls import path, include
from users import views as user_views


urlpatterns = [
  path('register/', user_views.UserRegisterView.as_view(), name='register'),
  path('profile/', user_views.UserProfileView.as_view(), name='profile'),
  path('login/', user_views.UserLoginView.as_view(), name='login'),
  path('logout/', user_views.UserLogoutView.as_view(), name='logout'),
  path('password-reset/', user_views.UserPasswordResetView.as_view(), name='password_reset'),
  path('password-reset/done/',user_views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
  path('password-reset-confirm/<uidb64>/<token>/', user_views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('password-reset-complete/', user_views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
