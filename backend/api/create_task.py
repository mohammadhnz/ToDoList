from flask import Blueprint
from flask import request, jsonify

import repository as task_repository

create_task_api = Blueprint('create_task_api', __name__)


@create_task_api.post('/api/v1/tasks/')
def create_task():
    name = request.json['name']
    description = request.json['description']
    task = task_repository.create_task(name, description)
    return jsonify({'id': task.id, 'name': task.name})
