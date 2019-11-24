# Questions Overflow

## Description

Questions Overflow is a question answering webapp.

## Installation

Installing the latest stable version is simple. But make sure first you have python install on your system.
You can use virtualenv or any wrapper to create Virtual Environment. I have used *pipenv*.

   `$ pip install pipenv`
   
[Check this for more information about pipenv](https://docs.pipenv.org/en/latest/)

## Install directly from git.
    $ git clone https://github.com/purkayasta/StackOverFlowLite.git
    $ cd Social_Boards
    $ pipenv install
    
## Make sure delete all the migrations in the migration folder and do database migration.
    $ python manage.py makemigrations
    $ python manage.py migrate
    
## Run the app by writting this commad.
    $ python manage.py runserver
