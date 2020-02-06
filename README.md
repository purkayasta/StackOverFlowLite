# Questions Overflow


## Description
StackOverflow-Lite is a question answering webapp (A lite version of [StackOverFlow](https://stackoverflow.com/))



## Home Screen:
![0](https://user-images.githubusercontent.com/12936435/73941488-91f43e80-4917-11ea-8534-019900fbe980.png)
## Question Detail Screen:
![1](https://user-images.githubusercontent.com/12936435/73941490-928cd500-4917-11ea-9fc8-35c636b65f0d.png)
## Login Screen:
![2](https://user-images.githubusercontent.com/12936435/73941485-915ba800-4917-11ea-9f82-5c2de97b7275.png)



## Motivation:
1. What if Stack Overflow was born before ajax or single page app :D
2. Also I wanted some hands of experience in Django :p

## Installation

Installing the latest stable version is simple. But make sure first you have python install on your system.
You can use virtualenv or any wrapper to create Virtual Environment. I have used *pipenv*.

   `$ pip install pipenv`
   
[Check this for more information about pipenv](https://docs.pipenv.org/en/latest/)

## Install directly from git.
    $ git clone https://github.com/purkayasta/StackOverFlowLite.git
    $ cd StackOverFlowLite
    $ pipenv install
    
## Make sure delete all the migrations in the migration folder and do database migration.
    $ python manage.py makemigrations
    $ python manage.py migrate
    
## Run the app by writing this command.
    $ python manage.py runserver

