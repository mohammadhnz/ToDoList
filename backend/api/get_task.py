from flask import Blueprint
from flask import request, jsonify

import repository as task_repository

get_task_api = Blueprint('get_task_api', __name__)


@get_task_api.get('/api/v1/tasks/')
def get_task():
    task_id = request.json['id']
    task = task_repository.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': f'No task found with id{task_id}'}), 204
    return jsonify({'id': task.id, 'name': task.name, 'deadline': task.deadline}), 200


