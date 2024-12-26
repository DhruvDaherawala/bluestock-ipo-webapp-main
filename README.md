## Follow these command to run this project:

git clone https://github.com/DhruvDaherawala/bluestock-ipo-webapp-main.git
```bash
cd bluestock-ipo-webapp
```
```bash
pip3 install -r requirements.txt
```
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py createsuperuser
```
```bash
python3 manage.py runserver
```
## How to connect a Django application to your PostgreSQL database

**Setting Up PostgreSQL Database**

1. **Install PostgreSQL:**

   Make sure PostgreSQL is installed on your system. You can download it from the official [PostgreSQL website](https://www.postgresql.org/download/).

2. **Create a PostgreSQL Database and User:**

   Once PostgreSQL is installed, create a new database and a user for your Django application. You can do this using the PostgreSQL command-line interface (`psql`) or a graphical tool like pgAdmin.

## Open your terminal and run the following commands:
```bash
CREATE DATABASE bluestock;
```
```bash
CREATE USER dhruv WITH PASSWORD '12345';
```
```bash
ALTER ROLE dhruv SET client_encoding TO 'utf8';
```
```bash
ALTER ROLE dhruv SET default_transaction_isolation TO 'read committed';
```
```bash
ALTER ROLE dhruv SET timezone TO 'UTC';
```
```bash
GRANT ALL PRIVILEGES ON DATABASE bluestock TO dhruv;
```
## Install PostgreSQL Adapter for Python
```bash
pip install psycopg2-binary
```
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluestock',
        'USER': 'dhruv',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
**Apply Migrations:**
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```
