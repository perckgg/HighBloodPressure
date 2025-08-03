.PHONY: help install dev test format lint migrate docker-build docker-up docker-down deploy

VENV_PATH := D:/Python_Environments/$(shell basename $(CURDIR))_env
PYTHON := $(VENV_PATH)/Scripts/python.exe
UVICORN := $(VENV_PATH)/Scripts/uvicorn.exe

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  dev          - Start development server"
	@echo "  test         - Run tests"
	@echo "  format       - Format code"
	@echo "  lint         - Lint code"
	@echo "  migrate      - Run database migrations"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-up    - Start Docker containers"
	@echo "  docker-down  - Stop Docker containers"

install:
	$(PYTHON) -m pip install -r requirements.txt

dev:
	$(UVICORN) src.app.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTHON) -m pytest tests/ -v --cov=src/app

format:
	$(PYTHON) -m black src/ tests/
	$(PYTHON) -m isort src/ tests/

lint:
	$(PYTHON) -m flake8 src/ tests/
	$(PYTHON) -m mypy src/

migrate:
	$(PYTHON) -m alembic upgrade head

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

deploy:
	docker-compose -f docker-compose.prod.yml up -d --build