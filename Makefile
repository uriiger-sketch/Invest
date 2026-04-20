.PHONY: install migrate ingest rank dashboard serve test fmt lint clean docker-build docker-up docker-down

install:
	pip install -e ".[dev]"

migrate:
	alembic upgrade head

ingest:
	python -m invest.cli ingest

rank:
	python -m invest.cli rank

train:
	python -m invest.cli train

dashboard:
	streamlit run src/invest/dashboard.py --server.port $${STREAMLIT_PORT:-8501}

serve:
	python -m invest.cli serve

test:
	pytest

fmt:
	ruff format src tests

lint:
	ruff check src tests

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +

docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-down:
	docker compose down
