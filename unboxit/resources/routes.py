from .movie import MoviesApi
from .user import RegisterUserApi
from .user import LoginUserApi
from .home import Home
from .login import Login
from .register import Register
from .dashboard import Dashboard, ViewDetails
from .imdb import GetMoviesByTitle, GetMoviesImagesByImdb, GetShowsByTitle, GetShowDetails, GetMovieDetails \
, GetMoviesImagesByImdb, GetShowImagesByImdb, GetSimilarMovies, GetSimilarShows


def initialize_routes(api):
    print(api)
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')
    api.add_resource(Home, '/')
    api.add_resource(Login, '/login')
    api.add_resource(Register, '/register')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(ViewDetails, '/view-details/<id>/<image>')
    api.add_resource(GetMoviesByTitle, '/get-movies-by-title/<title>', endpoint="get-movies-by-title")
    api.add_resource(GetMovieDetails, '/get-movie-details/<id>', endpoint="get-movie-details")
    api.add_resource(GetMoviesImagesByImdb, '/get-movies-images-by-imdb/<id>', endpoint="get-movies-images-by-imdb")
    api.add_resource(GetSimilarMovies, '/get-similar-movies/<id>', endpoint="get-similar-movies")
    api.add_resource(GetShowsByTitle, '/get-shows-by-title/<title>', endpoint="get-shows-by-title")
    api.add_resource(GetShowDetails, '/get-show-details/<id>', endpoint="get-show-details")
    api.add_resource(GetShowImagesByImdb, '/get-show-images-by-imdb/<id>', endpoint="get-show-images-by-imdb")
    api.add_resource(GetSimilarShows, '/get-similar-shows/<id>', endpoint="get-similar-shows")
