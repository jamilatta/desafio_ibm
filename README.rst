desafio_ibm
===========

Desafio IBM

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: GPLv3


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy desafio_ibm

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd desafio_ibm
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.


With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog


To access the e-mail during development tests

http://localhost:8025 (mailhog)

Components and technologies:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 * Módulo ``django.contrib.auth``
 * Módulo ``django.utils.translation``
 * Módulo ``django.contrib.auth.models.AbstractUser``
 * Templatetags
 * Generic views
 * Jquery
 * chzn-chosen select
 * Bootstrap
 * Docker
 * Docker-compose
 * Nginx
 * Celery
 * Postgres
 * I18N (Django)
 * Enviroment Variables
 * Markdown
 * Pip
 * gunicorn
 * CSS
 * Javascript
 * PGBouncer
 * Adminer (dev)
 * Mailhog
 * Redis
 * Docs
 * Code Style Black.

Docker
^^^^^^^^

To build the appplication:

.. code-block:: bash

    docker-compose -f local.yml build

To run the aplication with docker

.. code-block:: bash

    docker-compose -f local.yml up -d


Access with browser:

http://localhost:8000

