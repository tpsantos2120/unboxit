from .movie import MoviesApi
from .user import RegisterUserApi
from .user import LoginUserApi
from .home import Home
from .login import Login
from .register import Register
from .dashboard import Dashboard
from .imdb import GetMoviesByTitle, GetShowsByTitle, GetShowDetails, GetMovieDetails \
, GetMovieImages, GetShowImages, GetSimilarMovies, GetSimilarShows


def initialize_routes(api):
    print(api)
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')
    api.add_resource(Home, '/')
    api.add_resource(Login, '/login')
    api.add_resource(Register, '/register')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(GetMoviesByTitle, '/get-movies-by-title/<title>')
    api.add_resource(GetMovieDetails, '/get-movie-details/<id>')
    api.add_resource(GetMovieImages, '/get-movie-images/<id>')
    api.add_resource(GetSimilarMovies, '/get-similar-movies/<id>')
    api.add_resource(GetShowsByTitle, '/get-shows-by-title/<title>')
    api.add_resource(GetShowDetails, '/get-show-details/<id>')
    api.add_resource(GetShowImages, '/get-show-images/<id>')
    api.add_resource(GetSimilarShows, '/get-similar-shows/<id>')
