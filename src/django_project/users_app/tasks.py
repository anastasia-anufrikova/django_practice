from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

@shared_task
def notify_registration(user_id: int):
    admin_email = settings.DEFAULT_FROM_EMAIL
    user = User.objects.get(id=user_id)
    send_mail(
        subject='Регистрация успешна',
        message=f'Регистрация выполнена\n\n'
                f'Пользователь: {user.username}\n',

        from_email=admin_email,
        recipient_list=[user.email],
        fail_silently=False
    )
    return f'Пользователю {user.username} отправлено уведомление на почту {user.email}'
