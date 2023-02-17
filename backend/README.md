# T-WEB-800 BACKEND

## Setup

You must have **Docker** installed.

### Extra steps if you're on macos

> Install XCode from the App Store  
> Install pyenv with `brew install pyenv`  
> Install an older version of python with `pyenv install 2.7.18`

Make sure you have a database dump (ask a collegue !) in the `backend/db` folder, and rename it dump.sql

You can then download, build and prepare Docker by running the following command: `./run build`  
Make sure to close the terminal after running this command because it will be polluted with logs.

Finally, install Python required dependencies and load the DB dumb with : `./run prepare`

## Run

To get things running, you can use `./run run` and `./run stop` to stop it.  
This _run_ task will start the containers with _docker-compose_ :

- The Django Webservers
- One Celery Worker
- One Celery Heartbeat

If you're having a major issue, you can start the whole process over with `./run wipe`

### Python dependencies

If python dependencies were added or changed, you need to update them with `./run refresh`

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
- `./run start`: starts the containers
- `./run stop`: stops the containers
- `./run bash`: runs bash terminal on the django container
- `./run psql`: runs psql prompt on the postgres container
- `./run webserver`: shortcut for ./manage.py runserver 0.0.0.0:8000.
- `./run shell`: shortcut for ./manage.py shell_plus.
- `./run pip`: installs requirements with pip
- `./run makemigrations`: shortcut for ./manage.py makemigrations
- `./run migrate`: shortcut for ./manage.py migrate
- `./run test`: shortcut for pytest
- `./run loaddb`: loads database from the db/dump.sql file
- `./run resetdb`: clears the database
- `./run anonymize`: produces an anonymized dump from db/dump.sql at db/anonymized_dump.sql
- `./run deploy`: shortcut for devops/deploy.sh.
- `./run servers`: runs webserver
- `./run prepare`: runs pip and loaddb
- `./run format`: formats the code with black.
- `./run format-check`: checks whether the code has been formatted with black.

## Running pytest

You can run pytests in the entire project with ./run pytest. It uses the -s flag by default, so it will activate a debugger on ipdb.set_trace() calls.

Aditionaly, you can run a subset of tests by passing additional parameters:

- `./run pytest app_name` will only run tests within the app_name app
- `./run pytest app_name class_or_method_name` will only run tests within the app_name app and whose class or method name contains class_or_method_name

## VSCode setup

Visual Studio Code is the recommended IDE for development.

To enable autocomplete, code navigation and such, do the following:

- From the project's root folder, run `python3 -m venv venv` to create a Python virtual environment in the folder `venv`.
- In the project's VSCode settings, add the `python.pythonPath`; if the Python extension is already installed, VSCode should prompt you to add it automatically.
- Run `source ./venv/bin/activate`.
- In the same terminal, run `pip install -r backend/requirements-test.txt`.

Now, if you reload VSCode, you should have access to language-specific features such as autocompletion, jump to definition, find occurrences, etc.
