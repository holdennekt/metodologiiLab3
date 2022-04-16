FROM python:3.10-alpine

RUN apk add build-base

COPY requirements/backend.in /app/requirements/backend.in

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r app/requirements/backend.in

COPY . /app

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
