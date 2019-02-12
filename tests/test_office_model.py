import sys
import json
import unittest
from run import app

sys.path.append("app")

from app import *


class TestParty(unittest.TestCase):
    """method is used will be used to construct all our test"""
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {  # office data
                "id":1,
                "type":"senate",
                "name": "office of the senator",
        }
        self.da = { 
                "id":1,
                "type":"senate",
                "name": "office of the senator",
            }

    #  test case for creating a office
    def test_creating_office(self):
        response_data = self.client.post('/offices', data=json.dumps(self.data),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response_data.status_code, 201)
        self.assertIn(1, int(response_data.data))
        self.assertIn('office', str(response_data.data))
        self.assertIn('senate', str(response_data.data))
        self.assertEqual(response_data.get_json['status'], 201)

    def test_getting_all_offices(self):
        response_data = self.client.get(path='/offices', content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_getting_single_office(self):
        office = self.client.post(path='/offices', data=json.dumps(self.data), content_type="application/json")
        id = int(office.get_json('id'))
        path = '/offices/{}'.format(id)
        response_data = self.client.get(path, content_type="application/json")
        self.assertEqual(response_data.status_code, 200)

    def test_editing_an_office(self):
        office = self.client.post(path='/offices', data=json.dumps(self.data), content_type="application/json")
        id = int(office.get_json('id'))
        name = office.get_json('name')
        path = '/offices/{}/{}'.format(id, name)
        response_data = self.client.patch(path, data=json.dump(self.da), content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_deleting_a_office(self):
        office = self.client.post(path='/offices', data=json.dumps(self.data), content_type='application/json')
        id = int(office.get_json('id'))
        path = '/offices/{}'.format(id)
        response_data = self.client.delete(path, content_type='application/json')
        self.assertEqual(response_data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
