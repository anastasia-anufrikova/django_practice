from django.test import TestCase
from django.contrib.auth.models import User
from django.apps import apps


class ProfileModelCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_name', password="12345Yfcnz")

    def test_profile_creation(self):
        Profile = apps.get_model('users_app', 'Profile')
        profile_exists = Profile.objects.filter(user=self.user).exists()
        self.assertTrue(profile_exists)
