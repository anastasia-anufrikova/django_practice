FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

WORKDIR /app

RUN apt update && apt install make && apt-get install -y curl

#ENV PYTHONBUFFERED=1 \
#    PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml uv.lock README.md ./

COPY src/django_project/__init__.py ./src/django_project/

RUN uv sync --frozen

COPY . .
