from flask import Blueprint
from flask import request, jsonify

import repository as task_repository

delete_task_api = Blueprint('delete_task_api', __name__)


@delete_task_api.delete('/api/v1/tasks/')
def delete_task():
    task_id = request.json['id']
    task_repository.delete_task(task_id)
    return jsonify({'response': f'Task with id {task_id} has been deleted.'}), 204

