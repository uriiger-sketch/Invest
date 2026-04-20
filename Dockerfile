FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libgomp1 sqlite3 curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src
COPY alembic.ini ./
COPY alembic ./alembic

RUN pip install --upgrade pip && pip install .

EXPOSE 8501

CMD ["python", "-m", "invest.cli", "serve"]
