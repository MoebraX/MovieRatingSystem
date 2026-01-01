from repositories import *
from exceptions.service_exceptions import *

class MovieService():
    def __init__(self, movie_repository: MovieRepository,
                genre_repository: GenreRepository,
                director_repository: DirectorRepository,
                movierating_repository: MovieRatingRepository ):
        self.movie_repository = movie_repository
        self.genre_repository = genre_repository
        self.director_repository = director_repository
        self.movierating_repository = movierating_repository

    
    def calculate_ratings(self, id: int) -> dict[str, float | int | None]:
        movie = self.movie_repository.get(id)
        ratings_count = len(movie.ratings)
        if ratings_count == 0:
            return {"average_rating": None, "ratings_count": 0}
        average_rating = 0
        for rating in movie.ratings:
            average_rating += rating.score
        average_rating = average_rating/ratings_count
        return {"average_rating": average_rating, "ratings_count": ratings_count}
    
    def read_a_movie(self, id: int) -> Movie:
        movie = self.movie_repository.get(id)
        return movie
    
    def paginate_movies(self, page: int = 1, page_size: int = 10, all_movies: list[Movie] = []) -> dict:
        if all_movies == []:
            return {"page": page, "page_size": page_size, "total_items": 0, "items": all_movies}
        start = (page-1) * page_size
        finish = (page * page_size) 
        target_movies = all_movies[ start : finish ]
        return {"page": page, "page_size": page_size, "total_items": len(all_movies), "items": target_movies}
    
    def list_movies(self, page: int, page_size: int) -> dict:
        all_movies = self.movie_repository.get_all()
        return self.paginate_movies(page = page, page_size = page_size, all_movies = all_movies)
    
    def filter_movies(self, page: int, page_size: int, title: str, release_year: int, genre: str) -> dict:
        all_movies = self.movie_repository.filter(title = title, release_year = release_year, genre = genre)
        return self.paginate_movies(page = page, page_size = page_size, all_movies = all_movies)

    def add_movie(self,title: str,director_id: int, release_year: int | None, cast: str | None,genres: list[int]) -> Movie:
        movie = self.movie_repository.add(title = title, director_id = director_id, release_year = release_year, cast = cast)
        movie.genres = [self.genre_repository.get(genre_id) for genre_id in genres]
        self.movie_repository.session.commit()
        return movie

 


    
