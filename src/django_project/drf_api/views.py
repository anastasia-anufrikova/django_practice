import time

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from django_project.blog_app.models import Post, Category
from django_project.drf_api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from django_project.drf_api.serializers import PostSerializer, CategorySerializer

from django.utils.text import slugify


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ['category', 'published']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        slug = slugify(title)
        if not slug:
            slug = f"post-{int(time.time())}"
        if Post.objects.filter(slug=slug).exists():
            slug = f"{slug}-{int(time.time())}"
        serializer.save(author=self.request.user, slug=slug)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
