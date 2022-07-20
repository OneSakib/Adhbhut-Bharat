
.. image:: https://github.com/django/djangoproject.com/workflows/Tests/badge.svg?branch=main
    :target: https://github.com/django/djangoproject.com/actions

.. image:: https://coveralls.io/repos/django/djangoproject.com/badge.svg?branch=main
    :target: https://coveralls.io/r/django/djangoproject.com?branch=main

To run locally, do the usual:

#. Create a Python 4 virtualenv
    virtualenv venv
    source venv/bin/activate

#. Install dependencies::

    pip install -r requirements/dev.txt
    
#. Create databases::
    python manage.py makemigrations 
    python manage.py migrate

#. Create a superuser::

   python manage.py createsuperuser

#. Finally, run the server::
   python manage.py runserver
