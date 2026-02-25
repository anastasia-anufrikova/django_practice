from django.contrib.auth.models import User
from django.test import TestCase
from django.db import IntegrityError
from django_project.blog_app.models import Category, Post


class PostModelCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345Yfcnz')
        self.category = Category.objects.create(title='test_category', slug='test_category')
        self.post = Post.objects.create(title='test_title', slug='test_title', content='test_content', category=self.category, author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'test_title')
        self.assertEqual(self.post.slug, 'test_title')
        self.assertEqual(self.post.category, self.category)
        self.assertFalse(self.post.published)

    def test_post_str(self):
        self.assertEqual(str(self.post), 'test_title')

class CategoryModelCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='test_category', slug='test_category')

    def test_category_creation(self):
        self.assertEqual(self.category.title, 'test_category')
        self.assertEqual(self.category.slug, 'test_category')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'test_category')

    def test_category_slug_uniqueness(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(title='new_category', slug='test_category')
