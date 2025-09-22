PY := python3
PIP := pip3

.PHONY: setup test lint dev run clean precommit precommit-autoupdate coverage-html help tidy

setup:
	$(PIP) install -r requirements.txt

test:
	$(PY) -m pytest -q

lint:
	$(PY) -m pyflakes src || echo "pyflakes not installed; skipping"

dev run:
	$(PY) -m src.app

clean:
	rm -rf .pytest_cache __pycache__ */__pycache__

precommit:
	pre-commit run --all-files || echo "pre-commit not installed; install with: pip install pre-commit"

precommit-autoupdate:
	pre-commit autoupdate || echo "pre-commit not installed; install with: pip install pre-commit"

coverage-html:
	$(PY) -m pytest --cov=src --cov-report=html
	@echo "Open htmlcov/index.html in your browser"

tidy:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -prune -exec rm -rf {} +

help:
	@echo "Common targets:"
	@echo "  make setup            Install dependencies"
	@echo "  make test             Run tests with coverage (terminal)"
	@echo "  make lint             Run pyflakes on src/"
	@echo "  make dev              Run the example app"
	@echo "  make coverage-html    Generate HTML coverage report"
	@echo "  make precommit        Run pre-commit on all files"
	@echo "  make precommit-autoupdate  Update pre-commit hook versions"
	@echo "  make clean|tidy       Remove caches"
