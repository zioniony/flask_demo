#!/bin/bash
# start flask server
poetry run flask --app app.py run -p 8093&
flask_pid=$!
# start celery worker
poetry run celery -A celery_worker.celery_app worker --loglevel=INFO
state=$?
# kill flask server
kill -9 $flask_pid
# exit with celery worker state
exit $state
