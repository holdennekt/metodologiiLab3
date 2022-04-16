FROM python:3.10-buster

COPY . /app

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r app/requirements/backend.in

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
