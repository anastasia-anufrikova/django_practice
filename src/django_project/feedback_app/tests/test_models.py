from django.test import TestCase
from django_project.feedback_app.models import Feedback


class FeedbackModelCase(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(name='test_name', email='test_email', subject='test_subject', message='test_message')

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.name, 'test_name')
        self.assertEqual(self.feedback.email, 'test_email')
        self.assertEqual(self.feedback.subject, 'test_subject')
        self.assertEqual(self.feedback.message, 'test_message')

    def test_feedback_str(self):
        self.assertEqual(str(self.feedback), f'{'test_name'} - {'test_email'}')
