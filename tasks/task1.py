'''
use db indirectly in tasks by using current_app
'''
from celery_worker import celery_app
from flask import current_app
import time


@celery_app.task
def add_together(a: int, b: int) -> int:
    time.sleep(10)
    db = current_app.extensions['sqlalchemy']
    return {
        "value": a + b,
        "indirect_models": sorted(mdl._sort_key for mdl in db.Model.registry.mappers)
    }
