echo "Rest migrations and drop/create DB? Cannot be undone! (Hit CTRL-C to cancel)"
mysql -u root -p -Bse 'drop database example_lab; create database example_lab character set utf8;'
rm -rf example_lab/migrations/
# rm db.sqlite3
# mysql -u root -p -Bse 'create database example_lab character set utf8;'
python manage.py makemigrations example_lab
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

