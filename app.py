from app_factory import create_app
from blueprints.bp1 import bp, bp1
from blueprints.bp2 import bp2


app = create_app()
app.register_blueprint(bp)
app.register_blueprint(bp1, url_prefix="/bp1")
app.register_blueprint(bp2, url_prefix="/bp2")
