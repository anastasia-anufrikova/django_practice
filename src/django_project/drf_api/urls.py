from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_project.drf_api.views import PostViewSet, CategoryViewSet

app_name = 'drf_api'

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
