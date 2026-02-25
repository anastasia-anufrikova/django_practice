from django.urls import reverse
from django.test import TestCase

class ProfileViewCase(TestCase):
    def test_private_profile(self):
        response = self.client.get(reverse('users:profile_edit'))
        self.assertEqual(response.status_code, 302)
