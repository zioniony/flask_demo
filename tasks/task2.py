'''
use db directly in tasks
'''
from celery_worker import celery_app
from models import db
import time


@celery_app.task
def add_together(a: int, b: int) -> int:
    time.sleep(10)
    return {
        "value": a + b,
        "direct_models": sorted(mdl._sort_key for mdl in db.Model.registry.mappers)
    }
