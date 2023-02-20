# T-WEB-800 BACKEND

## Setup

You must have **Docker** installed.

Make sure you have a database dump (ask a collegue !) in the `backend/db` folder, and rename it dump.sql

You can then download, build and prepare Docker by running the following command: `./run build-back`  
Make sure to close the terminal after running this command because it will be polluted with logs.

Finally, load the DB dumb with : `./run prepare`

## Run

To get things running, you can use `./run back` and `./run stop-back` to stop it.  
This _run_ task will start the containers with _docker-compose_ :

- The Symfony main server

If you're having a major issue, you can start the whole process over with `./run wipe`

### Dependencies

If dependencies were added or changed, you need to update them with `./run refresh`

## Connect to local database

The docker container for postgres must be running for you to connect to the database.
The credentials and connection infos are:

- **User**: `postgres`
- **Password**: `postgresql__password`
- **Host**: `localhost`
- **Port**: `5436`
- **Database**: `djangoweb800`

## The runner script - ./run

- `./run run`: starts the containers and all backend processes
- `./run back`: starts the containers and all backend processes
- `./run start`: starts all the containers
- `./run stop`: stops the containers
- `./run bash`: runs bash terminal on the symfony container
- `./run psql`: runs psql prompt on the postgres container
- `./run startSymfony`: shortcut for symfony server:start (runned on the docker instance)
- `./run shell`: shortcut for ./manage.py shell_plus.
- `./run refresh`: installs dependencies
- `./run loaddb`: loads database from the db/dump.sql file
- `./run resetdb`: clears the database
- `./run servers`: runs webserver
- `./run prepare`: runs loaddb


## VSCode setup [to be done]

Visual Studio Code is the recommended IDE for development.

To enable autocomplete, code navigation and such, do the following:

- From the project's root folder, run `python3 -m venv venv` to create a Python virtual environment in the folder `venv`.
- In the project's VSCode settings, add the `python.pythonPath`; if the Python extension is already installed, VSCode should prompt you to add it automatically.
- Run `source ./venv/bin/activate`.
- In the same terminal, run `pip install -r backend/requirements-test.txt`.

Now, if you reload VSCode, you should have access to language-specific features such as autocompletion, jump to definition, find occurrences, etc.
