import json

from tests.base_test import BaseCase


class TestGetWatchlist(BaseCase):
    """
        Test cases for GET many records
    """

    def test_get_watchlists_successful(self):
        """
            Create user and insert record, then fetch it.
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

        response = self.app.post('/api/auth/register',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        token = response.json['token']

        payload_entry = json.dumps({
            "poster": "https://movie.poster.com",
            "media_type": "movies",
            "title": "Ad Astra",
            "description": "The near future,"
            + "a time when both hope and hardships drive"
            + "humanity to look to the stars and beyond."
            + "While a mysterious phenomenon menaces to"
            + "destroy life on planet Earth, astronaut Roy McBride"
            + "undertakes a mission across the immensity of space and"
            + "its many perils to uncover the truth about a lost"
            + "expedition that decades before boldly faced emptiness"
            + "and silence in search of the unknown.",
            "year": "2019",
            "release_date": "2019-09-17",
            "imdb_id": "tt2935510",
            "imdb_rating": "6.1",
            "vote_count": "4394",
            "popularity": "44.602",
            "youtube_trailer_key": "BsCNKuB93BA",
            "runtime": 123,
            "stars": [
                "Brad Pitt",
                "Tommy Lee Jones",
                "Ruth Negga",
                "John Ortiz",
                "Liv Tyler"
            ],
            "directors": [
                "Dan Bradley",
                "James Gray",
                "Sharron Reynolds-Enriquez",
                "Doug Torres",
                "Christina Fong",
                "Mark Valenzuela"
            ],
            "creators": []
        })

        response = self.app.post(
            '/api/watchlists',
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + response.json['token']},
            data=payload_entry)

        response = self.app.get(
            '/api/watchlists',
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + token})

        self.assertEqual(list, type(response.get_json()))
        self.assertEqual(200, response.status_code)

    def test_get_watchlists_empty_list(self):
        """
            Create user and register, provide no watchlist insertion
            get results back.
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

        response = self.app.post('/api/auth/register',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_register)

        token = response.json['token']
        response = self.app.get('/api/watchlists',
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer " + token})

        self.assertEqual(list, type(response.get_json()))
        self.assertEqual(200, response.status_code)

    def test_get_watchlists_not_authorized(self):
        """
            Perform logout and try access restricted routes.
        """

        response = self.app.get('/logout')
        response = self.app.get('/api/watchlists')

        self.assertEqual(200, response.status_code)
