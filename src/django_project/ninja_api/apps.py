from django.apps import AppConfig


class NinjaApiConfig(AppConfig):
    name = 'django_project.ninja_api'
    def ready(self):
        import ninja_api.signals # noqa
