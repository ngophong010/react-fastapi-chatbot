.PHONY: help install dev build test clean docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install all dependencies
	@echo "Installing server dependencies..."
	cd server && pip install -r requirements.txt
	@echo "Installing worker dependencies..."
	cd worker && pip install -r requirements.txt
	@echo "Installing client dependencies..."
	cd client && npm install

dev: ## Start development environment
	@echo "Starting development environment..."
	docker-compose up --build

build: ## Build all services
	@echo "Building all services..."
	docker-compose build

test: ## Run tests
	@echo "Running server tests..."
	cd server && python -m pytest tests/ -v
	@echo "Running client tests..."
	cd client && npm test -- --coverage --watchAll=false

lint: ## Run linting
	@echo "Linting server code..."
	cd server && python -m flake8 src/
	@echo "Linting client code..."
	cd client && npm run lint

format: ## Format code
	@echo "Formatting server code..."
	cd server && python -m black src/
	@echo "Formatting client code..."
	cd client && npm run format

docker-build: ## Build Docker images
	docker-compose build

docker-up: ## Start services with Docker
	docker-compose up -d

docker-down: ## Stop Docker services
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

clean: ## Clean up
	docker-compose down -v
	docker system prune -f