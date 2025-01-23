FROM python:3.12 AS builder

WORKDIR /src

COPY poetry.lock pyproject.toml ./

RUN apt update -y && \
    apt upgrade -y && \
    apt install build-essential -y && \
    pip install poetry==1.8.2 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction

FROM python:3.12-slim
USER root

ARG PYTHONPATH
ENV PYTHONPATH=$PYTHONPATH:/src
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONBUFFERED=1
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
ENV PYTHONDONTWRITEBYTECODE=1
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED
ENV PYTHONHASHSEED=0

COPY --from=builder --chown=root:root /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --chown=root:root ./ /src

WORKDIR /src
EXPOSE 8000

ENTRYPOINT ["python", "src/main.py", "web", "run"]