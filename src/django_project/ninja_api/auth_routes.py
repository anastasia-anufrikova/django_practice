from django.conf import settings
from django.contrib.auth import aauthenticate
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from ninja import Router
from ninja.errors import HttpError

from django_project.ninja_api.schemas import RegisterOutSchema, RegisterInSchema, ActivationOutSchema, LoginOutSchema, \
    LoginInSchema, EmailPayloadSchema

from django.contrib.auth.models import User

from django_project.ninja_api.utils import create_access_token


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

auth_router = Router(tags=['Authentication'])

@auth_router.post('/register', response=RegisterOutSchema)
def register(request, payload:RegisterInSchema) -> RegisterOutSchema:
    if User.objects.filter(email=payload.email).exists():
        raise HttpError(status_code=400, message='Email уже используется')
    if User.objects.filter(username=payload.username).exists():
        raise HttpError(status_code=400, message='Пользователь с таким именем уже существует')

    user = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        is_active=False
    )
        #return RegisterOutSchema(
        #    message='Регистрация успешна',
        #   username=user.username,
        #    email=user.email,
        #    id=user.id
        #)

    token_email(user)
    return {
        'message': 'Регистрация успешна',
        'username': payload.username,
        'email': payload.email,
        'id': user.id
    }

@auth_router.get('/activate/{uid}/{token}', response=ActivationOutSchema)
async def activate(request, uid:str, token:str) -> ActivationOutSchema:
    try:
        user_id = force_str(urlsafe_base64_decode(uid))
        user = await User.objects.aget(pk=user_id)
    except (TypeError, ValueError, User.DoesNotExist):
        return ActivationOutSchema(activated=False, message='Ошибка активации')

    if not default_token_generator.check_token(user, token):
        return ActivationOutSchema(activated=False, message='Ссылка устарела')
    user.is_active = True
    await user.asave()

    return ActivationOutSchema(activated=True, message='Учётная запись активирована')

@auth_router.post('/login', response=LoginOutSchema)
async def login(request, payload:LoginInSchema) -> LoginOutSchema:
    user = await aauthenticate(
        request=request,
        username=payload.username,
        password=payload.password
    )
    if user is None:
        return LoginOutSchema(success=False, message='Неверный логин или пароль')
    access_token =create_access_token(user.id, user.username)
    return LoginOutSchema(
        success=True,
        message='Авторизация успешна',
        username=user.username,
        email=user.email,
        id=user.id,
        is_staff=user.is_staff,
        access_token=access_token
    )

@auth_router.post('/resend-activation', response=ActivationOutSchema)
async def reactivate(request, payload: EmailPayloadSchema) -> ActivationOutSchema:
    try:
        user = await User.objects.aget(email=payload.email)
    except User.DoesNotExist:
        raise HttpError(status_code=400, message='Такого пользователя не существует')
    if not user.is_active:
        token_email(user)
        return ActivationOutSchema(activated=False, message='Новая ссылка направлена')

    return ActivationOutSchema(activated=True, message='Учётная запись уже активна')
