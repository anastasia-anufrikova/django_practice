from django.urls import path

from django_project.drf_api.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

app_name = 'drf_api'
urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail')
]
