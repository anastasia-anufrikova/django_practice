from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from django_project.blog_app.forms import PostForm, CategoryForm
from django_project.blog_app.models import Post, Category
import time


class IndexView(TemplateView):
    template_name = "blog_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(published=True).order_by("-created_at")[:5]
        return context

class PostListView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Список статей"
        return context

    def get_queryset(self):
        return self.model.objects.filter(published=True)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg ="post_slug"

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

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/create_category.html"

    def form_valid(self, form):
        form.instance.slug = f"post-{int(time.time())}"
        return super().form_valid(form)

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
