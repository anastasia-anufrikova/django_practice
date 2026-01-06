from django.core.management import BaseCommand, CommandError
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = 'Удаляет пост по id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='ID статьи', nargs='?')

    def handle(self, *args, **options):

        id = options['id'] or input("Введите id статьи: ")

        if not id:
            raise CommandError("Статьи с таким id не существует")

        id = int(id)

        post = Post.objects.get(
                id=id
            )
        title = post.title
        post.delete()

        self.stdout.write(self.style.SUCCESS(f'Пост "{title}" успешно удалён'))
