import unittest
import json
from app import app


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get('https://warm-retreat-38086.herokuapp.com/getusers')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)


    def test_get_user(self):
        response = self.app.get('https://warm-retreat-38086.herokuapp.com/searchuser/selva')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data['message'][0]['username'], 'selva')
        #self.assertEqual(data['message'][0]['department'], 'mech')

    def test_get_dept(self):
        response = self.app.get('https://guarded-springs-49761.herokuapp.com/searchdept/mech')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(data['message'][0].username, 'selva')
        #self.assertEqual(data['message'][0].department, 'mech')    

    def test_item_not_exist(self):
        response = self.app.get('https://warm-retreat-38086.herokuapp.com/searchuser/saravana')
        self.assertEqual(response.status_code, 404)


    def tearDown(self):
        # reset app.items to initial state
        pass


if __name__ == "__main__":
    unittest.main()
