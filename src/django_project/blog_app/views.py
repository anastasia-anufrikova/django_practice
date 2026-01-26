from django.shortcuts import get_object_or_404, render

from django_project.blog_app.models import Post, Category


def index(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")[:5]

    context = {
        "posts": posts
    }

    return render(request, "blog_app/index.html", context=context)

def post_list(request):
    posts = Post.objects.filter(published=True)
    context = {
        "posts": posts,
        "page_title": "Список статей",
    }
    return render(request, "blog_app/post_list.html", context=context)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        "post": post
    }
    return render(request, "blog_app/post_detail.html", context=context)

def categories_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "page_title": "Список категорий"
    }
    return render(request, "blog_app/categories_list.html", context=context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category, published=True)
    context = {
        "posts": posts,
        "page_title": "Статьи категории"
    }
    return render(request, "blog_app/post_list.html", context=context)
