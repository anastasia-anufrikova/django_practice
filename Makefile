run:
	uv run src/django_project/manage.py runserver

lint:
	python -m pre_commit run --all-files
