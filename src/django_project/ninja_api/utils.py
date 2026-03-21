import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def create_access_token(user_id: int, username: str) -> str:
    """Генерирует JWT Access Token для пользователя."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "sub": str(user_id),                # subject — кому выдан токен
        "username": username,
        "exp": expire,                      # expiration — когда истекает
        "iat": datetime.now(timezone.utc),  # issued at — когда выдан
    }
    # PyJWT сам кодирует словарь и возвращает строковый токен
    encoded_jwt = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def token_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    activation_url = f'http://127.0.0.1:8000/api/v2/auth/activate/{uid}/{token}'

    context = {
        "activation_url": activation_url,
        'user': user,
        'site_name': "Учебный блог на Django"
    }
    html_content = render_to_string('email/activation_email.html', context=context)

    message = EmailMessage(
        subject='Подтверждение регистрации',
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    message.content_subtype = 'html'
    message.send()
    return None
