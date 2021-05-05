from flask import make_response, url_for, redirect
from flask_jwt_extended.utils import unset_access_cookies
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from flask_restful import Resource
from unboxit.resources.utils.cache import cache


class Logout(Resource):
    """
        Logout user route.
    """
    def get(self):
        """
            Logout user and make sure there is a cookie inexistance.
            Either way log user out.
        """
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            res = make_response(redirect(url_for('home')))
            unset_access_cookies(res)
            cache.delete('watchlist_cache')
            cache.delete('recommendation_cache')
            cache.delete('trending_movies_cache')
            cache.delete('recommend')
            return res
        else:
            return redirect(url_for('home'))
