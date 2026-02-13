from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'social_link']
        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите информацию о себе',
                    'rows': 5
                }
            ),
            'social_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com',
            }),
        }
