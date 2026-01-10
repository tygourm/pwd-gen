init:
	uv sync --all-extras --frozen

tests: init
	uv run pytest -s

build: init
	uv build --wheel

write: init
	uv run ruff format --no-cache

check: init
	uv run ruff check --fix --no-cache && uv run ty check

clean:
	rm .coverage
	rm -rf dist/ .venv/ htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
