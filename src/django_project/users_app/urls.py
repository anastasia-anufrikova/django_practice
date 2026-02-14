from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from . import views

app_name = 'users'

urlpatterns = [
    path('profile_view/', views.ProfileView.as_view(), name='profile_view'),
    path('profile_edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='users_app/password_change.html', success_url=reverse_lazy('users:password_change_done')), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='users_app/password_change_done.html'), name='password_change_done'),
]
