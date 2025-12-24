from fastapi import FastAPI , status, Depends
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