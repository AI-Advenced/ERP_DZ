.PHONY: install run test clean build docker

# Installation
install:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Démarrage développement
run:
	. venv/bin/activate && python app/main.py

# Démarrage production
serve:
	. venv/bin/activate && gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker

# Tests
test:
	. venv/bin/activate && pytest

# Tests avec couverture
test-cov:
	. venv/bin/activate && pytest --cov=app tests/

# Nettoyage
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov

# Construction Docker
docker-build:
	docker build -t erp-algeria .

# Démarrage Docker
docker-run:
	docker run -p 8000:8000 erp-algeria

# Docker Compose
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

# Migration de la base de données
migrate:
	. venv/bin/activate && alembic upgrade head

# Création d'une nouvelle migration
migration:
	. venv/bin/activate && alembic revision --autogenerate -m "$(msg)"
