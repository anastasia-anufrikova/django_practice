from django import forms
from django_project.blog_app.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название статьи',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите содержимое статьи',
                    'rows': 5
                }
            )
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название категории',
                }
            )}
