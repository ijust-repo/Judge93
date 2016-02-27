from __future__ import absolute_import
from celery import Celery


celery = Celery('tasks', broker='redis://localhost:6379/0')
