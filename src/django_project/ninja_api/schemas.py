import datetime
from typing import Literal

from ninja import ModelSchema
from ninja import Schema
from pydantic import EmailStr

from django_project.blog_app.models import Post, Category


class PostInSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'author']


class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'published', 'created_at']


class FeedbackInSchema(Schema):
    name: str
    email: EmailStr
    subject: Literal['thanks', 'complaint', 'other']
    message: str

class FeedbackOutSchema(FeedbackInSchema):
    id: int
    created_at: datetime.datetime

class CategoryInSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['title']

class CategoryOutSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
