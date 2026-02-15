from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views
from .views import CustomLoginView, CustomPasswordChangeView

app_name = 'users'

urlpatterns = [
    path('profile_view/', views.ProfileView.as_view(), name='profile_view'),
    path('profile_edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='users_app/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='users_app/password_reset.html', email_template_name='users_app/password_reset_email.html',success_url = reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='users_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users_app/password_reset_confirm.html', success_url = reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='users_app/password_reset_complete.html'), name='password_reset_complete')
]
