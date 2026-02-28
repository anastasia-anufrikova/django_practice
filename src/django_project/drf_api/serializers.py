from rest_framework import serializers
from django_project.blog_app.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'author', 'published', 'created_at', 'category')
        read_only_fields = ['slug', 'author']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')
