.PHONY: install
install:
	pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt

.PHONY: install-dev
install-dev: install
	pip install -r requirements-dev.txt
	python setup.py develop

.PHONY: build
build:
	python setup.py build

.PHONY: lint
lint:
	flake8 chaosreliably/ tests/
	isort --check-only --profile black chaosreliably/ tests/
	black --check --diff chaosreliably/ tests/
	mypy chaosreliably/ tests/

.PHONY: format
format:
	isort --profile black chaosreliably/ tests/
	black chaosreliably/ tests/

.PHONY: tests
tests:
	pytest
