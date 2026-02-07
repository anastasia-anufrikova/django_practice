from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.id])

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Содержимое статьи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    def increase_views_count(self):
        self.views_count += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created_at', 'published']
