'''
use db directly in views
'''
from flask import Blueprint, request
from models import db
from tasks.task2 import add_together

bp2 = Blueprint('bp2', __name__)


@bp2.route('/models')
def show():
    return {
        "direct_models": sorted(mdl._sort_key for mdl in db.Model.registry.mappers)
    }


@bp2.route('/add', methods=["POST"])
def start_add() -> dict[str, object]:
    a = request.json.get("a")
    b = request.json.get("b")
    result = add_together.delay(a, b)
    return {"result_url": f"http://127.0.0.1:8093/result/{result.id}"}