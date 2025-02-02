set -o errexit 

pip install -r requrements.txt 

python manage.py collectstatic --noinput

python manage.py migrate 
if [[ $CREATE_SUPERUSER]]; then
    python manage.py createsuperuser --noinput
fi