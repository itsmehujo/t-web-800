# Epic Road Trip

## I'm not the reader kind, just want to get it to work quick
gotcha:
```shell
  cp ./.env.example ./.env
  sudo ./run setupLocalUrl
  ./run generateCerts
  ./run build
  # Ctr-C after it stops prompting
  ./run run
```
Then head to [Epic Road Trip local's website](https://epicroadtrip.local/) !

## The runner script - ./run

### Global

- `./run run`: starts back and front containers, starts postgres database and caddy
- `./run stop`: stops all containers
- `./run stopMisc`: stops caddy and postgres
- `./run bash app_name`: runs bash terminal on the app_name container (react, activities, hotels, main_app, maps, restaurants)
- `./run dependencies`: installs dependencies on all frontend and backend apps

### Frontend

- `./run front`: starts the caddy and react containers
- `./run stopFront`: stops the frontend containers
- `./run bash react`: runs bash terminal on the react container
- `./run frontDependencies`: installs dependencies

### Backend

- `./run back`: starts the containers and all backend processes
- `./run stopBack`: stops the backend containers
- `./run debug app_name`: starts outputing logs from requested app
- `./run makemigrations`: create migrations on all apps (interactive)
- `./run migrate`: runs migrate from all apps (interactive)
- `./run psql`: runs psql prompt on the postgres container
- `./run backDependencies`: installs dependencies

# [BACKEND] T-WEB-800

==If you already did setup for the frontend, you can move to the Run step==

## Setup

You must have **Docker** installed.
Run `cp ./.env.example ./.env`

## Setup Caddy

### Option 1

run `sudo ./run setupLocalUrl`  
--> You're good to go !

### Option 2

Edit the your local .env file and change all lines appended by 'URL' to either

- custom urls you setup on your machine
- localhost:port combination (other than 8000, 8001, 8002, 8003, 8004)

## Add local certificates to support SSL

run `./run generateCerts`

## Build the containers

You can then download, build and prepare Docker by running the following command: `./run build`  
Make sure to close the terminal after running this command.

## Run

To get things running, you can use `./run back` and `./run stopBack` to stop it.  
This _run_ task will start the containers with _docker-compose_ :

- caddy
- postgres database
- activities app
- hotels app
- main_app app
- maps app
- restaurants app

If you're having a major issue, you can start the whole process over with `./run wipe`

### Dependencies

If dependencies were added or changed, you need to update them with `./run backDependencies`

## Connect to local database

The docker container for postgres must be running for you to connect to the database.
The credentials and connection infos are, if not changed by your local env variable:

- **User**: `tweb800`
- **Password**: `@!ChangeMe!`
- **Host**: `localhost`
- **Port**: `5436`
- **Database**: `symfonyweb800`

## VSCode setup [to be done]

Visual Studio Code is the recommended IDE for development.

To enable autocomplete, code navigation and such, do the following:

- From the project's root folder, run `python3 -m venv venv` to create a Python virtual environment in the folder `venv`.
- In the project's VSCode settings, add the `python.pythonPath`; if the Python extension is already installed, VSCode should prompt you to add it automatically.
- Run `source ./venv/bin/activate`.
- In the same terminal, run `pip install -r backend/requirements-test.txt`.

Now, if you reload VSCode, you should have access to language-specific features such as autocompletion, jump to definition, find occurrences, etc.

# [FRONTEND] T-WEB-800

==If you already did setup for the backend, you can move to the Run step==

## Setup

You must have **Docker** installed.
Run `cp ./.env.example ./.env`

## Setup Caddy

# Option 1

run `sudo ./run setupLocalUrl`  
--> You're good to go !

# Option 2

Edit the your local .env file and change all lines appended by 'URL' to either

- custom urls you setup on your machine
- localhost:port combination (other than 8000, 8001, 8002, 8003, 8004)

## Add local certificates to support SSL

run `./run generateCerts`

## Build the containers

You can then download, build and prepare Docker by running the following command: `./run build`  
Make sure to close the terminal after running this command.

## Run

To get things running, you can use `./run front` and `./run stopFront` to stop it.  
This _run_ task will start the containers with _docker-compose_ :

- caddy
- react app

If you're having a major issue, you can start the whole process over with `./run wipe`

### Dependencies

If dependencies were added or changed, you need to update them with `./run frontDependencies`

## The runner script - ./run
