from django.http import HttpResponse
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
    response_content = '<h1>Список статей</h1> <ul>'
    for post in posts:
        response_content += f'<li><a href="/post/{post.slug}/">{post.title}</a> {post.created_at}</li>'
    response_content += '</ul>'
    response_content += '<a href = "/categories/">Назад к списку категорий</a>'
    return HttpResponse(response_content)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        "post": post
    }
    return render(request, "blog_app/post_detail.html", context=context)

def categories_list(request):
    all_categories = Category.objects.all()
    response_content = "<h1>Список категорий</h1><ul>"
    for category in all_categories:
        response_content += f'<li><a href="/categories/{category.id}/">{category.title}</a></li>'
    response_content += "</ul>"
    return HttpResponse(response_content)

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts_category = Post.objects.filter(category=category, published=True)
    if posts_category:
        content = f'<h1>{category.title}</h1><ul>'
        for post in posts_category:
            content +=  f'<li><a href="/post/{post.slug}/">{post.title}</a></li>'
        content += '</ul>'
    else:
        content = f'''<h1>{category.title}</h1>
                  <p>Статей пока нет</p>
                  '''
    content += '<hr><a href = "/categories/">Назад к списку категорий</a>'
    return HttpResponse(content)
