# ZZAZZO BackEnd

# Technology

* Database: Postgres SQL
* Language: Python3
* Framework: Django Rest Framework
* Task Scheduling: Celery

# How to run in local

Clone the project
    
    git clone -b zzazzo-backend https://github.com/zzazzo-limited/zzazzo.git

Then open terminal/cmd

    cd zzazzo_backend

make **.env** file based on **example.env**

make virtual env folder

for windows

    python -m venv venv

for linux/mac

    sudo apt install python3-venv -y
    python3 -m venv venv

after that active virtual environments

for windows

    . venv/Scripts/activate

for Linux/mac

    . venv/bin/activate

then install all requirements

    pip install -r requirements.txt

after that test db connection nd other error using dry migration

    python manage.py makemigrations --check --dry-run

if everything is ok then run migrations

    python manage.py makemigrations

Then migrate

    python manage.py migrate

then create a directory name static_local

    mkdir static_local

Then use collect static

    python manage.py collectstatic

after that create a superuser

    python manage.py createsuperuser

give information for superuser and after creating superuser you are full free to run test local server

just use

    python manage.py runserver