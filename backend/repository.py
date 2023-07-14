from models.task import Task


def create_task(task_name: str, description: str) -> Task:
    return Task(name=task_name, description=description).save()


def edit_task(task_id: int, fields_to_update):
    task = Task.tasks[task_id]
    task.update(**fields_to_update)
    return task


def delete_task(task_id: int):
    task = Task.tasks[task_id]
    task.delete()


def get_tasks_list():
    return list(Task.tasks.values())


def get_task_by_id(task_id: int):
    return Task.tasks.get(task_id, None)
