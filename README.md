# SimpleEasy

Minimal Python starter with tests.

## Quickstart
1. Install Python 3.10+.
2. Run `make setup` to install deps.
3. Run `make test` to execute tests.
4. Run `make dev` to print a greeting (uses `APP_NAME`).

Example: `APP_NAME=Alice make dev` → `Hello, Alice!`

## Requirements
- Python 3.10 or newer
- Pip and Make

## Pre-commit (optional)
1. Install: `pip install pre-commit`
2. Initialize: `pre-commit install`
3. Run on all files: `make precommit`

## Contributing
- Use PRs for changes; require passing CI.
- Suggested branch protection for `main`:
  - Require PR reviews (1+)
  - Require status checks (tests + lint) to pass
  - Restrict pushes to maintainers only
- Use Conventional Commits (`feat:`, `fix:`, `docs:`...).
