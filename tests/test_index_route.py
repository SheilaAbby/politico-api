import json
from .base_test import BaseTest


class TestOfficeModel(BaseTest):

    def test_index(self):
        """
        tests for landing  route
        """
        res = self.client.get('/api/v1/index', headers={'Content-Type': 'application/json'})
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'WELCOME TO POLITICO-API, VISIT https://politico-app-api.herokuapp.com/api/v1')
