# Makefile
install:
	uv sync --active

build:
	uv build
	
brain-games:
	uv run brain-games

package-install:
	uv tool install ~/dist/*.whl

lint:
	uv run ruff check brain_games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd