FROM python:3.12-rc-slim

RUN apt-get update && apt-get install -y \
  apt-transport-https \
  ca-certificates \
  build-essential \
  python-dev \
  gettext \
  libtiff5-dev \
  libjpeg62-turbo-dev \
  zlib1g-dev \
  libfreetype6-dev \
  liblcms2-dev \
  libwebp-dev \
  tcl8.6-dev \
  tk8.6-dev  \
  python-tk \
  libpq-dev \
  git \
  zip \
  unzip 

RUN python -m pip install -U pip

RUN mkdir -p /var/run

COPY ./django/requirements.txt /code/django/requirements.txt
COPY ./django/requirements-dev.txt /code/django/requirements-dev.txt

RUN pip install -r /code/django/requirements-dev.txt
RUN pip install -r /code/django/requirements.txt