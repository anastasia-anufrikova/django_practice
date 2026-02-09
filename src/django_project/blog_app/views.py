from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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

class CategoriesListView(ListView):
    model = Category
    template_name = "blog_app/categories_list.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Список категорий"
        return context

class CategoryDetailView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Статьи категории"
        return context

    def get_queryset(self):
        id_param = self.kwargs['category_id']
        return self.model.objects.filter(category=id_param,published=True)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog_app/create_post.html"

    def form_valid(self, form):
        form.instance.slug = f"post-{int(time.time())}"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"post_slug": self.object.slug})

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog_app/create_category.html"

    def form_valid(self, form):
        form.instance.slug = f"post-{int(time.time())}"
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog_app/create_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_edit"] = True
        return context

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"post_slug": self.object.slug})

class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse("blog:post_list")
