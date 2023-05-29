FROM python:3.11 as requirements

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim

WORKDIR /code

COPY --from=requirements /tmp/requirements.txt /code/requirements.txt

RUN apt install libxext-dev libx11-dev x11proto-gl-dev

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt