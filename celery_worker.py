from celery import Celery, Task
from app_factory import create_app


def celery_init_app(app) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            # 这里的 app 是 flask 的 app, 下述两行的作用是在 celery 的 task 中,
            # 可以正常使用 flask 的 current_app 变量
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    # broker 等配置也可从 app config 读取, 如果配置了的话
    celery_app.config_from_object(
        dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            include=[
                'tasks.task1',
                'tasks.task2',
            ]
        )
    )
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


flask_app = create_app()
celery_app = celery_init_app(flask_app)
