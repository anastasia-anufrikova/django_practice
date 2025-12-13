run:
	uv run src/django_project/manage.py runserver
pre-commit-check:
	uv run pre-commit run -a
