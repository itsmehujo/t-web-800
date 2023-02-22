FROM php:8.1.16-zts as development

RUN apt-get update && \
  apt-get install -y --no-install-recommends libssl-dev zlib1g-dev curl git unzip netcat libxml2-dev libpq-dev libzip-dev && \
  pecl install apcu && \
  docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql && \
  docker-php-ext-install -j$(nproc) zip opcache intl pdo_pgsql pgsql && \
  docker-php-ext-enable apcu pdo_pgsql sodium && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN curl -sS https://get.symfony.com/cli/installer | bash
RUN mv /root/.symfony5/bin/symfony /usr/local/bin/symfony

RUN pecl install xdebug-3.1.3 \
  && docker-php-ext-enable xdebug \
  && echo "xdebug.mode=debug" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
  && echo "xdebug.client_host=host.docker.internal" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

ARG APP_NAME

COPY ./$APP_NAME/composer.json /code/$APP_NAME/composer.json
COPY ./$APP_NAME/composer.lock /code/$APP_NAME/composer.lock

ENV CORS_ALLOW_ORIGIN='^https?://(${FRONTEND_URL}|localhost|127\.0\.0\.1)(:[0-9]+)?$'

WORKDIR /code/$APP_NAME
RUN composer install --prefer-dist --no-interaction --optimize-autoloader --no-scripts
