# Automation starter

[![CI](https://github.com/dguezm93/automation-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/dguezm93/automation-starter/actions/workflows/ci.yml)

A small Python CLI template for practical automation. The included example computes SHA-256 checksums without loading entire files into memory.

**Python 3.12+ · No runtime dependencies · MIT licensed**

## Quick start

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
automation-starter README.md
```

On Windows, activate the environment with `.venv\Scripts\activate`.

The command prints a JSON array containing the path, byte count, and SHA-256 of each input. You can pass multiple files; paths containing spaces must be quoted.

```sh
automation-starter README.md pyproject.toml
python -m automation_starter README.md
```

Exit code is `0` on success and `2` for invalid arguments or unreadable input. Errors go to stderr. If any input fails, no partial JSON result is printed. Input files are never changed.

Checksums detect changes when compared with a trusted value; they do not prove the source of a file. Files should remain unchanged while hashing.

## Development

```sh
python -m ruff check .
python -m ruff format --check .
python -m unittest discover -s tests -v
```

CI runs these checks on Python 3.12 and 3.13. Workflow actions are pinned to commit SHAs, permissions are read-only, and checkout credentials are not persisted. Dependabot checks development dependencies and GitHub Actions weekly.

## Use as a template

1. Select **Use this template** on GitHub.
2. Rename the package and command for your project.
3. Update this README, badges, ownership, and support details.
4. Replace the example with one small, useful behavior and tests.
5. Configure branch protection and security settings in the new repository; GitHub does not copy all repository settings from templates.
6. Add deployment only when its target, secrets, costs, monitoring, and rollback plan are known.

## Layout

```text
src/automation_starter/  CLI and streaming checksum logic
tests/                  Unit and command-line behavior tests
.github/workflows/      CI
.github/dependabot.yml  Dependency update policy
docs/                   Development and release checklists
```

## Before a production release

See [docs/RELEASING.md](docs/RELEASING.md). This repository is a starter, not a deployed service or a claim of production readiness.

Contributions follow the account's [shared guidelines](https://github.com/dguezm93/.github/blob/main/CONTRIBUTING.md). Report vulnerabilities using **Security → Report a vulnerability**.

## Español

Plantilla reutilizable para automatizaciones en Python. Incluye una herramienta de huellas SHA-256, pruebas, formato, análisis estático y CI. Consulta [docs/WORKFLOW.es.md](docs/WORKFLOW.es.md) para el flujo diario y las comprobaciones previas a publicar.
