# Rugby Pool App

This project is a small Django application. Below are quick steps to get it running locally.

## Install dependencies

It is recommended to use a virtual environment. Once activated, install Django:

```bash
pip install django
```

## Apply database migrations

Run the migrations to create the local SQLite database:

```bash
python manage.py migrate
```

## Run the development server

Start the application with:

```bash
python manage.py runserver
```

The server will be available at <http://127.0.0.1:8000/> by default.

## Run the tests

Execute the test suite with:

```bash
python manage.py test
```

