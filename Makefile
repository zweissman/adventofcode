# Run wsl to start a unix prompt
pc-run:
	clear; pre-commit run --all-files

pc-enable pc-on:
	pre-commit install

pc-disable pc-off:
	pre-commit uninstall

pc-update:
	pre-commit autoupdate

ruff:
	clear; ruff check --select I --fix --line-length=100 .; ruff format --line-length=100 .

mypy:
	clear; mypy --install-types --non-interactive --show-error-codes --ignore-missing-imports 2023/
