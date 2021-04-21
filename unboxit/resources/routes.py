from .logout import Logout
from .movie import MoviesApi
from .user import RegisterUserApi
from .user import LoginUserApi
from .home import Home
from .login import Login
from .register import Register
from .dashboard import Dashboard, DashboardSearch, ViewDetails
from .imdb import SearchMovies, GetMoviesImagesByImdb, SearchTvShows, GetShowDetails, GetMovieDetails \
, GetMoviesImagesByImdb, GetShowImagesByImdb, GetSimilarMovies, GetSimilarShows


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')
    api.add_resource(Home, '/')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(Register, '/register')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(DashboardSearch, '/dashboard/search')
    api.add_resource(ViewDetails, '/view-details/')
    api.add_resource(SearchMovies, '/search/movies/<title>')
    api.add_resource(GetMovieDetails, '/get-movie-details/<id>', endpoint="get-movie-details")
    api.add_resource(GetMoviesImagesByImdb, '/get-movies-images-by-imdb/<id>', endpoint="get-movies-images-by-imdb")
    api.add_resource(GetSimilarMovies, '/get-similar-movies/<id>', endpoint="get-similar-movies")
    api.add_resource(SearchTvShows, '/search/tv-shows/<title>')
    api.add_resource(GetShowDetails, '/get-show-details/<id>', endpoint="get-show-details")
    api.add_resource(GetShowImagesByImdb, '/get-show-images-by-imdb/<id>', endpoint="get-show-images-by-imdb")
    api.add_resource(GetSimilarShows, '/get-similar-shows/<id>', endpoint="get-similar-shows")
