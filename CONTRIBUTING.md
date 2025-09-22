# Contributing

Thank you for your interest in improving SimpleEasy. This guide summarizes how to set up, make changes, and submit pull requests.

## Getting Started
- Requirements: Python 3.10+, Pip, Make, Git.
- Clone: `git clone https://github.com/leandro1416/SimpleEasy.git && cd SimpleEasy`
- Install deps: `make setup`
- (Optional) Pre-commit: `pip install pre-commit && pre-commit install`
- Run tests: `make test`
- Lint: `make lint`

## Workflow
- Create a feature branch: `git checkout -b feat/<short-name>`
- Make focused commits using Conventional Commits (e.g., `feat:`, `fix:`, `docs:`).
- Keep PRs small and self-contained; update/add tests as needed.
- Ensure CI passes (tests + lint). Coverage must be ≥ 80%.

## Project Layout
- Source: `src/`
- Tests: `tests/` (mirror `src/` structure). Name tests `test_*.py`.
- Scripts/automation: `Makefile`, GitHub Actions in `.github/workflows/`.
- Contributor guide: `AGENTS.md` and this `CONTRIBUTING.md`.

## Running Locally
- App example: `APP_NAME=Alice make dev`
- Coverage HTML: `make coverage-html` → open `htmlcov/index.html`.

## Pull Requests
- Provide a clear description; link issues (e.g., `Closes #123`).
- Include tests for new/changed behavior.
- Update docs if the public interface changes.
- Screenshots for any UI-related changes.

## Security
- Do not commit secrets. Use `.env.example` to document variables.
- Report sensitive issues privately if applicable.

## Code Review
- CODEOWNERS auto-requests reviewers. Address feedback promptly.
- Squash or rebase to maintain a clean history when merging.
