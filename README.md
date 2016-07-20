TO RUN LOCALLY:

git clone https://github.com/sjstone2838/hrsw.git

cd hrsw

Set a local environment variable 'DJANGO_SECRET_KEY' to a random string of your choice

python manage.py makemigrations

python manage.py migrate

python manage.py runserver --settings=platform.settings.local

TO ADD RANDOMLY-GENERATED PROJECT:

python manage.py createProject <userCount: int> --settings=platform.settings.local