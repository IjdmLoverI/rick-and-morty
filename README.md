# rick-and-morty
to run:
celery -A rick_and_morty_api beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

docker run -d -p 6379:6379 redis

celery -A rick_and_morty_api worker -l INFO
