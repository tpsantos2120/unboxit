from .logout import Logout
from .movie import MovieApi, MoviesApi
from .user import RegisterUserApi, ResetPassword
from .user import LoginUserApi
from .home import Home
from .app_api import Dashboard, DashboardSearch
from .imdb import Recommend, SearchMovieDetails, SearchMovies, SearchTrendingMovies, SearchTrendingShows,\
SearchTvShows, SearchShowDetails, SearchMovieDetails



def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movie/<id>')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')
    api.add_resource(ResetPassword, '/api/auth/reset')
    api.add_resource(Home, '/')
    api.add_resource(Logout, '/logout')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(DashboardSearch, '/dashboard/search')
    api.add_resource(SearchMovies, '/search/movies/<title>')
    api.add_resource(SearchMovieDetails, '/search/movie/details/<id>')
    api.add_resource(SearchTvShows, '/search/shows/<title>')
    api.add_resource(SearchShowDetails, '/search/show/details/<id>')
    api.add_resource(SearchTrendingMovies, '/search/trending/movies')
    api.add_resource(SearchTrendingShows, '/search/trending/shows')
    api.add_resource(Recommend, '/recommend')




