from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from django_project.blog_app.models import Category, Post

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345Yfcnz')
        self.category = Category.objects.create(title='test_category', slug='test_category')
        self.post = Post.objects.create(title='test_title', slug='test_title', content='test_content', category=self.category, author=self.user, published=True)

    def test_index_status_code(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertTemplateUsed(response, 'blog_app/index.html')

    def test_index_contains_post(self):
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, 'test_title')

    def test_post_detail_status_code(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.slug]))
        self.assertTemplateUsed(response, 'blog_app/post_detail.html')

    def test_post_detail_context(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.slug]))
        self.assertEqual(response.context['post'], self.post)

    def test_post_detail_404(self):
        response = self.client.get(reverse('blog:post_detail', args=["Page-does-not-exist"]))
        self.assertEqual(response.status_code, 404)

    def test_index_not_have_unpublished(self):
        Post.objects.create(title='test_title2', slug='test_title2', content='test_content',
                                        category=self.category, author=self.user, published=False)
        response = self.client.get(reverse('blog:index'))
        self.assertNotContains(response, 'test_title2')
        self.assertContains(response, 'test_title')


class CategoryViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345Yfcnz')
        self.category = Category.objects.create(title='test_title', slug='test_title')
        self.post = Post.objects.create(title='test_post', slug='test_post', content='test_content',
                                        category=self.category, author=self.user, published=True)

    def test_index_contains_category(self):
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, 'test_title')

    def test_category_filtering(self):
        self.cat1 = Category.objects.create(title='test_1', slug='test_1')
        self.cat2 = Category.objects.create(title='test_2', slug='test_2')
        self.post1 = Post.objects.create(title='post_1', slug='post_1', content='test_content',
                                        category=self.cat1, author=self.user, published=True)
        self.post2 = Post.objects.create(title='post_2', slug='post_2', content='test_content',
                                         category=self.cat2, author=self.user, published=False)
        response = self.client.get(reverse('blog:category_detail', kwargs={'category_id': self.cat1.id}))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_category_detail_404(self):
        response = self.client.get(reverse('blog:category_detail', kwargs={'category_id': 9999}))
        self.assertEqual(response.status_code, 404)
