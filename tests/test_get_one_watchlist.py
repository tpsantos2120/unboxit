import json

from tests.base_test import BaseCase

class TestGetOneWatchlist(BaseCase):

    def test_get_one_watchlist_successful(self):
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
            "description": "The near future, a time when both hope and hardships drive humanity to look to the stars and beyond. While a mysterious phenomenon menaces to destroy life on planet Earth, astronaut Roy McBride undertakes a mission across the immensity of space and its many perils to uncover the truth about a lost expedition that decades before boldly faced emptiness and silence in search of the unknown.",
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

        response = self.app.post('/api/watchlists',
                                 headers={"Content-Type": "application/json"},
                                 data=payload_entry)

        response = self.app.get('/api/watchlists',
                                headers={"Content-Type": "application/json"})

        id = response.json[0]['_id']['$oid']
        response = self.app.get('/api/watchlist/'+ id,
                                headers={"Content-Type": "application/json"})

        self.assertEqual(dict, type(json.loads(response.get_json())))
        self.assertEqual(200, response.status_code)

    def test_get_one_watchlist_not_authorized(self):
    

        response = self.app.get('/api/watchlist/sdfsdf',
                                headers={"Content-Type": "application/json"})

        self.assertEqual("Not authorized.", response.json['message'])
        self.assertEqual(401, response.status_code)