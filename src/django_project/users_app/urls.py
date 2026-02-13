from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
path('profile_view/', views.ProfileView.as_view(), name='profile_view'),
path('profile_edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
]
