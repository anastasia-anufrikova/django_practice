from django.test import TestCase
from django.urls import reverse

from django_project.feedback_app.models import Feedback

class FeedbackViewTest(TestCase):
    form_data = {
        'name': 'test_user',
        'email': 'user@example.com',
        'subject': 'other',
        'message': 'Текст'
    }

    def test_feedback_sent(self):
        response = self.client.post(reverse('feedback:feedback_page'), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Feedback.objects.count(), 1)

    def test_feedback_error(self):
        form_data = {
            'name': 'test_user',
            'email': 'user@example.com',
            'subject': 'Тема',
            'message': 'Текст'
        }
        response = self.client.post(reverse('feedback:feedback_page'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.count(), 0)
        self.assertIn("subject", response.context["form"].errors)
