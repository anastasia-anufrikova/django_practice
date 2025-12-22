from django.contrib import admin

from django_project.blog_app.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'published','created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_field = ('title', 'content')
    list_filter = ('author', 'published', 'created_at')
