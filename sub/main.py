from __future__ import absolute_import
from celery import Celery

APP = Celery('memory',
    broker='amqp://guest:guest@localhost/',
    backend='rpc://',
    include=["memory.sub.tasks"]
)
# APP.start()