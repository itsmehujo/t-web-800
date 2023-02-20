FROM node:lts-alpine3.17 as development

RUN mkdir -p /var/run

WORKDIR /code/react

COPY package.json /code/react/package.json
COPY package-lock.json /code/react/package-lock.json

RUN npm ci
COPY . /code/react

CMD ["npm", "start"]