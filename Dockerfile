FROM python:3.11.0-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /code/

CMD ["poetry", "run", "python", "main.py"]
