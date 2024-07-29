.DEFAULT_GOAL := help

help:
	@echo "Makefile for StarlightStation"
	@echo ""
	@echo "Targets:"
	@echo "  build      Build the Docker image"
	@echo "  run       Run the application"
	@echo "  test      Run the tests"
	@echo "  lint      Run the linter"
	@echo "  format    Format the code"

build:
	docker-compose build

run:
	docker-compose up

test:
	pytest

lint:
	black --check.
	isort --check.

format:
	black.
	isort.
