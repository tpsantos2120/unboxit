from .movie import MoviesApi
from .user import RegisterUserApi
from .user import LoginUserApi


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')

