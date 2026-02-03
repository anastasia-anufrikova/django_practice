from django.shortcuts import get_object_or_404, render, redirect

from django_project.blog_app.forms import PostForm, CategoryForm
from django_project.blog_app.models import Post, Category
import time


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

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = f"post-{int(time.time())}"
            new_post.save()
            return redirect("blog:post_detail", new_post.slug)
    else:
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "blog_app/create_post.html", context=context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.slug = f"post-{int(time.time())}"
            new_category.save()
            return redirect("blog:category_detail", category_id=new_category.id)
    else:
        form = CategoryForm()

    context = {
        "form": form,
    }
    return render(request, "blog_app/create_category.html", context=context)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.save()
            return redirect("blog:post_detail", edited_post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "is_edit": True,
    }

    return render(request, "blog_app/create_post.html", context=context)
