#! /bin/bash

killall -9 python
killall -9 celery

celery -A project.tasks worker --loglevel=info &
python run_old.py test

