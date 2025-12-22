run:
	uv run src/django_project/manage.py runserver

lint:
	uv run pre-commit run --all
