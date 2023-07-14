from flask import Blueprint
from flask import jsonify

import repository as task_repository

list_tasks_api = Blueprint('list_tasks_api', __name__)


@list_tasks_api.get('/api/v1/tasks/list')
def get_tasks_list():
    tasks = task_repository.get_tasks_list()
    tasks_data = [
        {'id': task.id, 'name': task.name, 'description': task.description}
        for task in tasks
    ]
    return jsonify(tasks_data)
