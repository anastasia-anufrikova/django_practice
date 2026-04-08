from django.db.models.signals import post_save
from django.dispatch import receiver

from django_project.blog_app.models import Post


@receiver(post_save, sender=Post)
def invalidate_post_cache(sender, instance, **kwargs):
    from django_project.ninja_api.tasks import invalidate_post_cache_task
    invalidate_post_cache_task.delay(instance.id)
