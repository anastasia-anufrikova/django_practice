from celery import shared_task
from django.core.cache import cache


@shared_task
def invalidate_post_cache_task(post_id: int):
    cache_key = f'api_post_{post_id}'
    cache.delete(cache_key)
    try:
        cache.incr('posts_version')
    except (ValueError, TypeError):
        cache.set('posts_version', 1)
