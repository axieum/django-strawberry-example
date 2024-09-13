# django-strawberry-example

A reproduction of Strawberry GraphQL namespaces in a Django project.

```sh
poetry install
poetry run manage.py runserver
```

## Development

### `poetry run manage.py runserver`

Runs the [Django] server at http://localhost:8000/.

### `poetry run mypy`

Runs the static type checks in files.

### `poetry run ruff check --fix`

Lints and corrects errors in files.

### `poetry run ruff format`

Formats and corrects style errors in files.

[django]: https://djangoproject.com/
