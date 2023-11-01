'''
use db indirectly in views by using current_app
'''
from flask import Blueprint, current_app, request
from celery.result import AsyncResult
from tasks.task1 import add_together

bp = Blueprint('root', __name__)
bp1 = Blueprint('bp1', __name__)


@bp.route("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


@bp1.route('/models')
def show():
    db = current_app.extensions['sqlalchemy']
    return {
        "indirect_models": sorted(mdl._sort_key for mdl in db.Model.registry.mappers)
    }


@bp1.route('/add', methods=["POST"])
def start_add() -> dict[str, object]:
    a = request.json.get("a")
    b = request.json.get("b")
    result = add_together.delay(a, b)
    return {"result_url": f"http://127.0.0.1:8093/result/{result.id}"}
