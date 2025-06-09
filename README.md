# Rugby Pool App

This project is a small Django application. Below are quick steps to get it running locally.

## Install dependencies

It is recommended to use a virtual environment. Once activated, install the
project dependencies:

```bash
pip install -r requirements.txt
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

## Docker

You can also run the application in a Docker container. Build the image with:

```bash
docker build -t rugbypoolapp .
```

Start the container (migrations run automatically):

```bash
docker run -p 8000:8000 rugbypoolapp
```

