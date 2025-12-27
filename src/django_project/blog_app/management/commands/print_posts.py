from django.core.management import BaseCommand
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = 'Выводит список постов'

    def handle(self, *args, **options):
        posts = Post.objects.all()

        #self.stdout.write(f"{posts}")
        if not posts.exists():
            self.stdout.write(self.style.WARNING('Посты не найдены'))

        for post in posts:
            self.stdout.write(f"{post.id} {post.title} {post.created_at:%Y-%m-%d}")
