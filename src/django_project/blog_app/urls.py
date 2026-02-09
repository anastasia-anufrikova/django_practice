from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
    path('category/create/', views.CategoryCreateView.as_view(), name='create_category'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
    ]
