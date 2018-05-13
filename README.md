Hedge-Dash-web3
===============

Hedge dashboard with web3 integration. Demo application is live at https://powerful-caverns-66638.herokuapp.com.

Run on Development Machine
--------------------------

To run the app on your local machine, you need Python 3.5+, PostgreSQL, and [MailHog](https://github.com/mailhog/MailHog) (to capture outgoing emails) installed on your computer.

1.  Create and activate virtualenv:

        python3 -m venv venv
        . venv/bin/activate

2.  Install package dependencies:

        pip install -r requirements.txt

3.  Create new PostgreSQL database and user:

        $ psql postgres
        psql (9.6.5)
        Type "help" for help.

        postgres=# CREATE DATABASE hedge;
        postgres=# CREATE USER hedge WITH PASSWORD 's3cr3t';
        postgres=# ALTER ROLE hedge SET client_encoding TO 'utf8';
        postgres=# ALTER ROLE hedge SET default_transaction_isolation TO 'read committed';
        postgres=# ALTER ROLE hedge SET timezone TO 'UTC';
        postgres=# ALTER USER hedge CREATEDB;
        postgres=# GRANT ALL PRIVILEGES ON DATABASE hedge TO hedge;

4.  Create new `.env` file:

        cp .env.example .env

5.  Fill in the required values below and you can leave the others empty:

        POSTGRES_DBNAME=hedge
        POSTGRES_USER=hedge
        POSTGRES_PASSWORD=s3cr3t

6.  Run database migration:

        ./manage.py migrate

7.  Run MailHog to capture all outgoing emails:

        MailHog

8.  Run the development server:

        ./manage.py runserver 3000

Deploy on Dedicated Server
--------------------------

Make sure that you have [Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

1.  Create new `.env` file:

        cp .env.example .env

    **Fill in all of the values**.

2.  Build and run the containers:

        docker-compose build && docker-compose up -d


Deploy on Heroku
----------------

Make sure you have a Heroku account and [Heroku CLI](https://cli.heroku.com/) is installed on your computer.

1.  Login to Heroku:

        heroku login

2.  Create new Heroku app:

        heroku create

3.  Set the environment variables:

        heroku config:set DJANGO_SETTINGS_MODULE=config.settings.heroku
        heroku config:set DJANGO_SECRET_KEY=<value>
        heroku config:set MAILGUN_API_KEY=<value>
        heroku config:set MAILGUN_SENDER_DOMAIN=<value>
        heroku config:set DEFAULT_FROM_EMAIL=<value>

4.  Push code to server:

        git push heroku master

5.  Run database migrations and optionally create a user:

        heroku run ./manage.py migrate
        heroku run ./manage.py createsuperuser

6.  Open the app:

        heroku open
