To run the application:
1. Set the environment variables:
   * SECRET_KEY
   * DB_NAME 
   * vladimir
   * DB_PASSWORD
   * DB_HOST
   * DB_PORT
   * ALLOWED_HOSTS
2. Install [poetry](https://python-poetry.org/). Recommended way:
```console
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
Alternative way (not recommended):
```console
$ pip install --user poetry
```

3. Install project's dependencies:
```console
$ poetry install
```