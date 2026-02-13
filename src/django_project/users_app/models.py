from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(verbose_name='Биография')
    social_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
