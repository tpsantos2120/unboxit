from unboxit.resources.forgot_password import ForgotPasswordReset
from .logout import Logout
from .watchlist import WatchlistApi, WatchlistsApi
from .user import ForgotPassword, RegisterUserApi, ResetPassword
from .user import LoginUserApi
from .home import Home
from .app_api import Dashboard, DashboardSearch
from .imdb import Recommend, SearchMovieDetails, SearchMovies, SearchTrendingMovies, SearchTrendingShows,\
SearchTvShows, SearchShowDetails, SearchMovieDetails



def initialize_routes(api):
    api.add_resource(WatchlistsApi, '/api/watchlists')
    api.add_resource(WatchlistApi, '/api/watchlist/<id>')
    api.add_resource(RegisterUserApi, '/api/auth/register')
    api.add_resource(LoginUserApi, '/api/auth/login')
    api.add_resource(ResetPassword, '/api/auth/reset')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ForgotPasswordReset, '/reset/password/<token>')
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




