from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    name = 'django_project.blog_app'
    def ready(self):
        import blog_app.signals  # noqa
