release: sh -c 'python manage.py migrate; python manage.py loaddata */fixtures/*.json; python manage.py seed --mode=refresh;'
web: gunicorn project_django.wsgi --log-file -