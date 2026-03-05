from django.http import HttpResponse
from ninja import NinjaAPI

from django_project.blog_app.models import Post, Category
from django_project.feedback_app.models import Feedback
from django_project.ninja_api.schemas import PostOutSchema, PostInSchema, FeedbackOutSchema, FeedbackInSchema, \
    CategoryOutSchema, CategoryInSchema

from django.utils.text import slugify

router = NinjaAPI(version='1.0.0', title='Ninja API blog', description='Блог на Django Ninja')

@router.get('/ping')
def ping(request) -> dict[str, bool]:
    return {'pong': True}

@router.get('/posts', response=list[PostOutSchema])
async def posts_list(request, search: str | None=None, category_id: int | None=None) -> list[PostOutSchema]:
    qs = Post.objects.all()
    if search:
        qs = qs.filter(title__icontains=search)

    if category_id:
        qs = qs.filter(category=category_id)

    return [post async for post in qs]

@router.get('/posts/{post_id}/', response=PostOutSchema)
async def post_get(request, post_id:int) -> PostOutSchema | HttpResponse:
    try:
        post = await Post.objects.aget(pk=post_id)
        return post
    except Post.DoesNotExist:
        return router.create_response(request, {'detail': 'Статья не найдена'}, status=404)

@router.post('/posts', response=PostOutSchema)
async def create_post(request, payload: PostInSchema) -> PostOutSchema:
    data = payload.model_dump()
    data['author_id'] = data.pop('author')
    data['category_id'] = data.pop('category')
    return await Post.objects.acreate(**data, slug=slugify(payload.title))

@router.post('/feedback', response=FeedbackOutSchema)
async def create_feedback(request, payload:FeedbackInSchema) -> FeedbackOutSchema:
    return await Feedback.objects.acreate(**payload.model_dump())

@router.get('/categories', response=list[CategoryOutSchema])
async def categories_list(request, search_title: str | None=None) -> list[CategoryOutSchema]:
    qs = Category.objects.all()
    if search_title:
        qs = qs.filter(title__icontains=search_title)

    return [category async for category in qs]

@router.get('/categories/{category_id}/', response=CategoryOutSchema)
async def category_get(request, category_id:int) -> CategoryOutSchema | HttpResponse:
    try:
        category = await Category.objects.aget(pk=category_id)
        return category
    except Category.DoesNotExist:
        return router.create_response(request, {'detail': 'Категория не найдена'}, status=404)

@router.post('/categories', response=CategoryOutSchema)
async def create_category(request, payload: CategoryInSchema) -> CategoryOutSchema:
    data = payload.model_dump()
    return await Category.objects.acreate(**data)

@router.delete('/categories/{category_id}/')
async def delete_category(request, category_id:int):
    try:
        category = await Category.objects.aget(pk=category_id)
        await category.adelete()
        return f'Категория {category_id} успешно удалена'

    except Category.DoesNotExist:
        return router.create_response(request, {'detail': 'Категория не найдена'}, status=404)
