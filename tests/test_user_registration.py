import json

from tests.base_test import BaseCase


class TestUserRegistration(BaseCase):
    """
        Test cases for registering users.
    """

    def test_successful_registration(self):
        """
            Attempt registering and check for succcesful repsonse.
        """
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

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_register_with_non_existing_field(self):
        """
            Attempt registering user with extra fields,
            expeting a 400 status code. 
        """
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

        self.assertEqual('Request is missing required fields',
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_register_without_email(self):
        """
            Attempt registering without email expected to get status 500.
        """
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

        self.assertEqual('Something went wrong internally',
                         response.json['message'])
        self.assertEqual(500, response.status_code)

    def test_registering_already_existing_user(self):
        """
            Attempt registering user that already exists.
        """

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

    def test_register_user_without_payload(self):
        """
            Attempt to registering without any registration details.
        """

        response = self.app.post(
            '/api/auth/register', headers={"Content-Type": "application/json"})

        self.assertEqual('Something went wrong internally',
                         response.json['message'])
        self.assertEqual(500, response.status_code)
