# django_microservices_boilerplate
###A boilerplate project for Django microservices with user CRUD operations, signup, login, JWT authentication, password management, permissions, and group management.

## Setup

The first thing to do is to clone the repository:

Run : git clone https://github.com/cis-muzahid/django_microservices_boilerplate.git

Create a virtual environment to install dependencies in and activate it:

RUN: $ virtualenv -p python3.12 env_name


RUN:$ source env_name/bin/activate


Then install the dependencies:


RUN:(env_name)$ pip install -r requirements.txt


Note the `(env_name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:

Migrate the database
sh
(env_name)$ python manage.py migrate


Go to the root DIR:
sh
(env_name)$ python manage.py runserver

And navigate to `http://127.0.0.1:8000/`.