release: python manage.py migrate
web: gunicorn companies.wsgi --log-file -