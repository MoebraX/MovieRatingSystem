from fastapi import FastAPI , status, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from db.session import *
from services.services import *
from exceptions.controller_exceptions import *

app = FastAPI()

# Function for injecting session to repository and repository to service
def get_user_service(session: Session = Depends(get_db)):
    movie_repository = MovieRepository(session)
    genre_repository = GenreRepository(session)
    director_repository = DirectorRepository(session)
    movierating_repository = MovieRatingRepository(session)
    service = MovieService(movie_repository, genre_repository, director_repository, movierating_repository)
    return service

#List and paginate all movies
# @app.get("/api/v1/movies" , status_code = status.HTTP_200_OK)
# def api_list_movies(page: int = Query(1), page_size: int = Query(10), service: MovieService = Depends(get_user_service)):
#     try:
#         paginated_movies = service.list_movies(page=page, page_size=page_size)
#         movies = paginated_movies["items"]
#         total_items = paginated_movies["total_items"]
#         items = []

#         for movie in movies:
#             ratings = service.calculate_ratings(id=movie.id)
#             genres=[]
#             for genre in movie.genres:
#                 genres.append(genre.name)
#             new_item = {
#                 "id": movie.id,
#                 "title": movie.title,
#                 "release_year": movie.release_year,
#                 "director": {
#                     "id": movie.director.id,
#                     "name": movie.director.name
#                 } if movie.director else None,
#                 "genres": genres,
#                 "average_rating": ratings["average_rating"],
#                 "ratings_count": ratings["ratings_count"]
#             }
#             items.append(new_item)

#         return {
#             "status": "success",
#             "data": {
#                 "page": page,
#                 "page_size": page_size,
#                 "total_items": total_items,
#                 "items": items
#             }
#         }
    
#     except Exception as e:
#         return JSONResponse(
#             status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
#             content = {
#                 "status": "failure",
#                 "message": str(e)
#             }
#         )

#Filter movies
@app.get("/api/v1/movies" , status_code = status.HTTP_200_OK)
def api_list_movies(page: int = Query(1),
                    page_size: int = Query(10),
                    title: str = Query(None),
                    release_year: str = Query(None),
                    genre: str = Query(None),
                    service: MovieService = Depends(get_user_service)):
    try:
        paginated_movies = service.filter_movies(page=page, page_size=page_size, title = title, release_year = release_year, genre = genre)
        movies = paginated_movies["items"]
        total_items = paginated_movies["total_items"]
        items = []

        for movie in movies:
            ratings = service.calculate_ratings(id=movie.id)
            genres = []
            for genre in movie.genres:
                genres.append(genre.name)
            new_item = {
                "id": movie.id,
                "title": movie.title,
                "release_year": movie.release_year,
                "director": {
                    "id": movie.director.id,
                    "name": movie.director.name
                } if movie.director else None,
                "genres": genres,
                "average_rating": round(ratings["average_rating"],2),
                "ratings_count": ratings["ratings_count"]
            }
            items.append(new_item)

        return {
            "status": "success",
            "data": {
                "page": page,
                "page_size": page_size,
                "total_items": total_items,
                "items": items
            }
        }

    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
            content = {
                "status": "failure",
                "error": {
                    "code": 422,
                    "message": "Invalid release_year"
                }
            }
        )
    
#Find a specific movie
@app.get("/api/v1/movies/{movie_id}" , status_code = status.HTTP_200_OK)
def api_movie_description(movie_id: int, service: MovieService = Depends(get_user_service)):
    try:
        movie = service.read_a_movie(movie_id)
        ratings = service.calculate_ratings(id=movie.id)
        genres = []
        for genre in movie.genres:
            genres.append(genre.name)
        new_item = {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "director": movie.director,
            "genres": genres,
            "cast": movie.cast,
            "average_rating": round(ratings["average_rating"],2),
            "ratings_count": ratings["ratings_count"]
            }
        return {
            "status": "success",
            "data": new_item
        }
    
    except MovieNotFound:
            return JSONResponse(
            status_code = status.HTTP_404_NOT_FOUND,
            content = {
                "status": "failure",
                "error": {
                    "code": 404,
                    "message": "Movie not found"
                }
            }
        )
    
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {
                "status": "failure",
                "error": {
                    "code": 500,
                    "message": str(e)
                }
            }
        )
    