from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from django.utils.text import slugify
import time

from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = 'Создаёт новую статью'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Название статьи', nargs='?')
        parser.add_argument('content', type=str, help='Содержание поста', nargs='?')


    def handle(self, *args, **options):

        title = options['title'] or input("Введите название статьи: ")
        content = options['content'] or input("Введите текст статьи: ")
        author = User.objects.first()

        if not author:
            raise CommandError("Сначала создайте пользователя!")

        slug = slugify(title)
        if not slug:
            slug = f"post-{int(time.time())}"
        if Post.objects.filter(slug=slug).exists():
            slug = f"{slug}-{int(time.time())}"

        try:
            post = Post.objects.create(
                title=title,
                content=content,
                author=author,
                slug=slug
            )

            self.stdout.write(self.style.SUCCESS(f'Пост "{post.title}" успешно создан'))
        except Exception as e:
            raise CommandError(f'Ошибка при создании поста: {e}')
