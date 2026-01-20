from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django_project.blog_app.models import Post, Category


def index(request):
    return HttpResponse('<h1>Мой блог</h1>')

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
    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.author.username}</p>
    <div>{post.content}</div>
    <hr>
    <a href="/post_list/">Назад ко всем статьям</a>
    <hr>
    <a href = "/categories/{post.category.id}/">Назад к статьям категории</a>
    '''
    return HttpResponse(content)

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
    content = f'<h1>{category.title}</h1><ul>'
    for post in posts_category:
        content +=  f'<li><a href="/post/{post.slug}/">{post.title}</a></li>'
    content += '</ul>'
    content += '<a href = "/categories/">Назад к списку категорий</a>'
    return HttpResponse(content)
