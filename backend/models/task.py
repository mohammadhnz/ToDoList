from datetime import datetime


class Task:
    tasks = dict()
    last_id = 1

    def __init__(self, name: str, description: str):
        self.id = None
        self.name = name
        self.description = description

    def save(self):
        self.id = Task.last_id
        Task.last_id += 1
        Task.tasks[self.id] = self
        return self

    def delete(self):
        del Task.tasks[self.id]

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise Exception(f'Invalid field, task has no {key} field.')
            setattr(self, key, value)

    def delete(self):
        del Task.tasks[self.id]
