from flask import Flask

from api.create_task import create_task_api
from api.delete_task import delete_task_api
from api.get_task import get_task_api
from api.list_tasks import list_tasks_api
from api.update_task import update_task_api

app = Flask(__name__)

app.register_blueprint(create_task_api)
app.register_blueprint(get_task_api)
app.register_blueprint(delete_task_api)
app.register_blueprint(list_tasks_api)
app.register_blueprint(update_task_api)


@app.get('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
