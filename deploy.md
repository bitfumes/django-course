manage.py check --deploy

1. secret key
2. debug
3. database
    pip install dj-database-url
    pip install psycopg2-binary
    import dj_database_url
    dj_database_url.config(conn_max_age=500)
4. serving static files
    static root
    pip install whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
5. HTTP Server
    pip install gunicorn
6. export requirements

7. For Heroku
    procfile
        web: gunicorn projectName.wsgi --log-file -
8. Create Heroku app and Add Allowed hosts