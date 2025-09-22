# Repository Guidelines

This document is a concise contributor guide for this repository. It favors clear structure, short explanations, and actionable steps. If something seems off or missing, open an issue or PR to improve it.

## Project Structure & Module Organization
- `src/` – application/library source code (create per feature/module).
- `tests/` – automated tests mirroring `src/` structure.
- `scripts/` – helper scripts (dev tasks, data setup).
- `assets/` – static files (images, fixtures).
- `README.md` – user-facing overview and quickstart.
Example module layout: `src/<package>/<feature>/` with tests in `tests/<feature>/test_*.{js,py,ts}`.

## Build, Test, and Development Commands
- `make setup` – install dependencies and set up local env.
- `make build` – compile/build the project into `dist/`.
- `make test` – run the full test suite with coverage.
- `make lint` – run linters and format checks.
- `make dev` – start local dev server or watch mode.
If `make` isn’t available, provide equivalent package or language commands in the README.

## Coding Style & Naming Conventions
- Indentation: 2 spaces (JS/TS), 4 spaces (Python). Keep lines ≤100 chars.
- Filenames: `kebab-case` for JS/TS files, `snake_case` for Python.
- Types/Classes: `PascalCase`; variables/functions: `camelCase` (JS/TS) or `snake_case` (Python).
- Use formatters/linters: Prettier + ESLint for JS/TS; Black + Ruff for Python.

## Testing Guidelines
- Mirror `src/` structure in `tests/`.
- Name tests `test_*.py` (PyTest) or `*.spec.ts` / `*.test.ts` (Jest/Vitest).
- Aim for ≥80% line coverage on changed code; include edge cases.
- Run locally via `make test` before opening a PR.

## Commit & Pull Request Guidelines
- Commits: Conventional Commits style recommended: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.
- Keep commits small and focused; include rationale in the body when useful.
- PRs: provide a clear description, link issues (`Closes #123`), note breaking changes, add screenshots for UI, and update docs/tests.
- Pass CI (build, lint, tests) before requesting review.

## Security & Configuration Tips
- Do not commit secrets; use `.env.example` for required variables.
- Review dependencies regularly; prefer pinned versions.
- Follow least-privilege for tokens/keys used in local testing.
