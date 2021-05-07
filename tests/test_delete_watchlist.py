import json

from tests.base_test import BaseCase


class TestDeleteWatchlist(BaseCase):
    """
        Test cases for DELETE request
    """

    def test_delete_watchlist_successful(self):
        """
            Register user, insert a movie to watchlist, then get watchlist id,
            and delete entry.
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

        payload_entry = json.dumps({
            "poster": "https://movie.poster.com",
            "media_type": "movies",
            "title": "Ad Astra",
            "description": "The near future, a time when both hope and"
            + "hardships drive humanity to look to the stars and beyond."
            + "While a mysterious phenomenon menaces to destroy life on"
            + "planet Earth, astronaut Roy McBride undertakes a mission across"
            + "the immensity of space and its many perils to uncover the truth"
            + "about a lost expedition that decades"
            + "before boldly faced emptiness"
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
            headers={"Content-Type": "application/json"},
            data=payload_entry)

        response = self.app.get(
            '/api/watchlists',
            headers={"Content-Type": "application/json"})

        id = response.json[0]['_id']['$oid']

        response = self.app.delete(
            '/api/watchlist/' + id,
            headers={"Content-Type": "application/json"})

        self.assertEqual("Movie was deleted successfully.",
                         response.json['message'])
        self.assertEqual(200, response.status_code)

    def test_delete_watchlist_no_id(self):
        """
            Create user and insert movie, but provide no valid ID
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

        payload_entry = json.dumps({
            "poster": "https://movie.poster.com",
            "media_type": "movies",
            "title": "Ad Astra",
            "description": "The near future, a time"
            + "when both hope and hardships drive humanity"
            + "to look to the stars and beyond. While a"
            + "mysterious phenomenon menaces to destroy life"
            + "on planet Earth, astronaut Roy McBride undertakes"
            + "a mission across the immensity of space and its many"
            + "perils to uncover the truth about a lost expedition that"
            + "decades before boldly faced emptiness and silence in"
            + "search of the unknown.",
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
            headers={"Content-Type": "application/json"},
            data=payload_entry)

        response = self.app.get(
            '/api/watchlists',
            headers={"Content-Type": "application/json"})

        response = self.app.delete(
            '/api/watchlist/' + "notvalid",
            headers={"Content-Type": "application/json"})

        self.assertEqual("Entry with given id doesn't exist",
                         response.json['message'])
        self.assertEqual(400, response.status_code)
