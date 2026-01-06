from django.core.management import BaseCommand, CommandError
from django.utils.text import slugify

from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = 'Обновляет название статьи по ID'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID статьи', nargs='?')

    def handle(self, *args, **options):

        post_id = options['id'] or input("Введите id статьи: ")

        if not post_id:
            raise CommandError("ID не был введён")

        try:
            post = Post.objects.get(id=int(post_id))
        except Post.DoesNotExist:
            raise CommandError(f"Статья с ID {post_id} не найдена в базе данных")
        except ValueError:
            raise CommandError("ID должен быть числом")

        post.title = input("Введите новое название статьи: ")
        if not post.title:
            raise CommandError("Название не может быть пустым")

        post.slug = slugify(post.title) or f"post-{post.id}"
        post.save()

        self.stdout.write(self.style.SUCCESS(f'Название "{post.title}" успешно присвоено посту {post.id}'))
