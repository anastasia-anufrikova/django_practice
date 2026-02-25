run:
	uv run src/django_project/manage.py runserver

lint:
	python -m pre_commit run --all-files

makemigrations:
	uv run src/django_project/manage.py makemigrations

migrate:
	uv run src/django_project/manage.py migrate

createsuperuser:
	uv run src/django_project/manage.py createsuperuser

posts:
	uv run src/django_project/manage.py print_posts

published:
	uv run src/django_project/manage.py print_published_posts

create:
	uv run src/django_project/manage.py create_post

delete:
	uv run src/django_project/manage.py delete_post

update:
	uv run src/django_project/manage.py update_post

test_blog_app:
	uv run src/django_project/manage.py test blog_app

test_feedback_app:
	uv run src/django_project/manage.py test feedback_app

test:
	uv run src/django_project/manage.py test

test_verbose:
	uv run src/django_project/manage.py test -v 2

test_users_app:
	uv run src/django_project/manage.py test users_app
