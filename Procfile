release: sh -c 'python manage.py migrate; find -L . -name "*.json" -exec python manage.py loaddata {} \; python manage.py seed --mode=refresh;'
web: gunicorn project_django.wsgi --log-file -