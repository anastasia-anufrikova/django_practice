from django_project.blog_app.models import Category, Post
from django.contrib.auth.models import User


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all()
    }

def blog_stats_processor(request):
    return {
        'total_posts': Post.objects.all().count(),
        'total_users': User.objects.all().count()
    }
