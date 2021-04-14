from .movie import MoviesApi
from .user import RegisterUserApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(RegisterUserApi, '/api/auth/register')
