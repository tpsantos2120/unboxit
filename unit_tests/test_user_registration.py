import json

from unit_tests.base_test import BaseCase


class TestUserRegistration(BaseCase):

    def test_successful_registration(self):
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

        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"}, data=payload_register)

        print(response)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_register_with_non_existing_field(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        email = "darth@darkside.com"
        password = "force1234"
        hobby = "kill people"
        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password,
            "hobby": hobby
        })

        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"}, data=payload_register)

        print(response)

        self.assertEqual('Request is missing required fields',
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_register_without_email(self):
        first_name = "Darth"
        last_name = "Vader"
        username = "darkside"
        password = "force1234"
        payload_register = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "password": password,
        })

        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"}, data=payload_register)

        print(response)

        self.assertEqual('Something went wrong internally',
                         response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_registering_already_existing_user(self):

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
        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"}, data=payload_register)

        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"}, data=payload_register)

        self.assertEqual(
            'User with given email address already exists', response.json['message'])
        self.assertEqual(400, response.status_code)
