from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя',
        })
    )

    email = forms.EmailField(
        label='Email для связи',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш email',
        })
    )

    message = forms.CharField(
        label='Ваше обращение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Напишите ваше обращение',
            'rows': 5
        })
    )
