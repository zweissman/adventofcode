# Run `wsl` to start a unix prompt on Windows

LINE_LENGTH = 120
TEST_ROOT = adventofcode
CHECK_ROOT = 2015

# Activating the shell usually calls `source`. When running on Windows via WSL, just use `.`
# Example: . /mnt/d/development/adventofcode/.venv/bin/activate
shell:
	clear; pip install --upgrade pip && pip install pipenv && pipenv shell && pipenv sync

update:
	clear; pipenv install && pipenv install --dev && pipenv sync

graph:
	clear; pipenv graph

lock:
	clear; pipenv lock

clean:
	echo "Removing temp files..."
	find . -type d \( -name ".pytest_cache" -o -name "__pycache__" -o -name ".pyc" \) -exec rm -r {} \+

# requires `pip install pytest pytest-cov`
coverage test:
	clear; pipenv run pytest --cov=${TEST_ROOT} --cov-branch --cov-report=html:cov_html --cov-report term-missing --no-header

# requires `pip install ruff`
ruff:
	clear;
	ruff check --select I --fix --line-length=${LINE_LENGTH} ${CHECK_ROOT};
	ruff format --line-length=${LINE_LENGTH} ${CHECK_ROOT}

# requires `pip install mypy`
mypy:
	clear; mypy --install-types --non-interactive --show-error-codes --ignore-missing-imports ${CHECK_ROOT}

# requires `pip install pylint`
pylint lint:
	clear; pre-commit run pylint

# requires `pip install pre-commit`
pc-run:
	clear; pre-commit run --all-files

pc-enable pc-on:
	pre-commit install

pc-disable pc-off:
	pre-commit uninstall

pc-update:
	pre-commit autoupdate
