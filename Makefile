PY := python3
PIP := pip3

.PHONY: setup test lint dev run clean precommit

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
