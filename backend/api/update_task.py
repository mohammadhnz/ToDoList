from flask import Blueprint
from flask import request, jsonify

import repository as task_repository

update_task_api = Blueprint('update_task_api', __name__)


@update_task_api.put('/api/v1/tasks/')
def update_task():
    task_id = request.json['id']
    task = task_repository.edit_task(task_id, request.json)
    if not task:
        return jsonify({'error': f'No task found with id{task_id}'}), 204
    return jsonify({'id': task.id, 'name': task.name, 'deadline': task.deadline}), 200
