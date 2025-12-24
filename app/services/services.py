from repositories import *
from exceptions import service_exceptions

class MovieService():
    def __init__(self, movie_repository: MovieRepository,
                genre_repository: GenreRepository,
                director_repository: DirectorRepository,
                movierating_repository: MovieRatingRepository ):
        self.movie_repository = movie_repository
        self.genre_repository = genre_repository
        self.director_repository = director_repository
        self.movierating_repository = movierating_repository