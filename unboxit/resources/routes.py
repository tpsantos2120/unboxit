from .watchlist import WatchListApi
from .user import RegisterUserApi
from .user import LoginUserApi


def initialize_routes(api):
    api.add_resource(WatchListApi, '/api/watchlist')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')

