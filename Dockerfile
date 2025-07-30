FROM python:3.13.5-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . /app
RUN uv sync --locked
CMD ["uv", "run", "fastapi", "run", "app/app.py", "--port", "80"]