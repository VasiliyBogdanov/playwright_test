lint:
	@flake8 --exclude .venv
testUI:
	@pytest -vvs tests/UI_tests/site
.PHONY: lint testUI