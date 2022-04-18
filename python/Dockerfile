FROM python:3.10-bullseye

WORKDIR app

COPY requirements/backend.in requirements/backend.in

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r requirements/backend.in

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
