from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('categories/', views.categories_list, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('create_post/', views.post_create, name='create_post'),
    path('category/create/', views.CategoryCreateView.as_view(), name='create_category'),
    ]
