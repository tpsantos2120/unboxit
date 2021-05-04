import json

from unit_tests.base_test import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        email = "darth@darkside.com"
        password = "force1234"

        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        })

        payload_login = json.dumps({
            "email": email,
            "password": password
        })

        response = self.app.post('/api/auth/register',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_login)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        email = "darth@darkside.com"
        password = "force1234"

        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        })

        email = "luke@skywalker.com"

        payload_login = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_login)

        self.assertEqual("Invalid username or password",
                         response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        email = "darth@darkside.com"
        password = "force1234"

        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        })

        password = "dark1234"

        payload_login = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_login)

        self.assertEqual("Invalid username or password",
                         response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_without_payload(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        email = "darth@darkside.com"
        password = "force1234"

        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        })

        payload_login = json.dumps({})

        response = self.app.post('/api/auth/signup',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        response = self.app.post('/api/auth/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_login)

        self.assertEqual("Invalid username or password",
                         response.json['message'])
        self.assertEqual(401, response.status_code)
