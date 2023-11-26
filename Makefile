pc-run:
	pre-commit run --all-files

pc-enable:
	pre-commit install

pc-disable:
	pre-commit uninstall
