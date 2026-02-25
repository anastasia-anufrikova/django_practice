from django.test import TestCase

from django_project.blog_app.forms import PostForm, CategoryForm
from django_project.blog_app.models import Category


class PostFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='test_category', slug='test_category')

    def test_valid_form(self):
        data = {
            'title': 'test_title',
            'content': 'test_content',
            'category': self.category
        }

        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_title(self):
        data = {
            'title': '',
        }

        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_empty_content(self):
        data = {
            'title': 'test_title',
        }

        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

class CategoryFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'test_title',
        }

        form = CategoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_title(self):
        data = {
            'title': '',
        }

        form = CategoryForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
