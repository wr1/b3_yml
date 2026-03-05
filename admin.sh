#!/usr/bin/env bash
# b3-yml admin script – run after cfold unfold

> out.txt

echo "=== ruff format & check ===" >> out.txt
ruff format >> out.txt 2>&1
ruff check --fix >> out.txt 2>&1

echo "\n=== git commits ===" >> out.txt

# pyproject.toml
git add pyproject.toml
git commit pyproject.toml -m 'chore: add pytest config and cov to b3-yml' || true

# README.md
git add README.md
git commit README.md -m 'docs: document testing workflow' || true

# tests/__init__.py
git add tests/__init__.py
git commit tests/__init__.py -m 'test: add tests package' || true

# tests/test_datasets.py
git add tests/test_datasets.py
git commit tests/test_datasets.py -m 'test: add smoke tests for data helpers and YAMLs' || true

# admin.sh (self-update)
git add admin.sh
git commit admin.sh -m 'chore: update admin.sh for new test files' || true

echo "\n=== pytest ===" >> out.txt
uv run pytest -v >> out.txt 2>&1 || true

echo "\nadmin.sh finished – see out.txt" | tee -a out.txt
