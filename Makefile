PY := python3
PIP := pip3

.PHONY: setup test lint format typecheck dev run serve test-server clean precommit precommit-autoupdate coverage-html help tidy

setup:
	$(PIP) install -r requirements.txt

test:
	PYTHONPATH=src $(PY) -m pytest -q

lint:
	ruff check src tests

format:
	ruff format src tests

dev run:
	$(PY) -m src.app

serve:
	$(PIP) install -r requirements-server.txt
	uvicorn src.server:app --reload --port 8000

clean:
	rm -rf .pytest_cache __pycache__ */__pycache__

precommit:
	pre-commit run --all-files || echo "pre-commit not installed; install with: pip install pre-commit"

precommit-autoupdate:
	pre-commit autoupdate || echo "pre-commit not installed; install with: pip install pre-commit"

coverage-html:
	PYTHONPATH=src $(PY) -m pytest --cov=src --cov-report=html
	@echo "Open htmlcov/index.html in your browser"

tidy:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -prune -exec rm -rf {} +

help:
	@echo "Common targets:"
	@echo "  make setup            Install dependencies"
	@echo "  make test             Run tests with coverage (terminal)"
	@echo "  make lint             Run Ruff checks"
	@echo "  make format           Format code with Ruff"
	@echo "  make dev              Run the example app"
	@echo "  make serve            Run FastAPI server on :8000"
	@echo "  make coverage-html    Generate HTML coverage report"
	@echo "  make precommit        Run pre-commit on all files"
	@echo "  make precommit-autoupdate  Update pre-commit hook versions"
	@echo "  make clean|tidy       Remove caches"
typecheck:
	mypy src
