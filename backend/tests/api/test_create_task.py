from api.create_task import create_task_api

import json
import unittest

from flask import Flask


class CreateTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(create_task_api)
        self.client = self.app.test_client()

    def test_create_task(self):
        payload = {'name': 'Finish project', 'description': '2023-07-31'}
        response = self.client.post('/api/v1/tasks/', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertEqual(data['name'], payload['name'])
        self.assertEqual(data['description'], payload['description'])