from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя отправителя', unique=True)
    email = models.EmailField(verbose_name='Email отправителя')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Отправлено')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} - {self.email}'
