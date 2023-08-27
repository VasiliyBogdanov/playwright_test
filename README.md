# Playwright homework

## Installation

#### Tested on Python 3.9 ✓

1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. playwright install chromium

## Usage

##### Run tests

```
pytest tests/UI_tests/site
```

or

```
make testUI
```

##### Lint

```
flake8 --exclude .venv
```

or

```
make lint
```