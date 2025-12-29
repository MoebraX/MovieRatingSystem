from typing import Optional
from sqlalchemy.orm import joinedload

from .repository_schema import *
from exceptions.repository_exceptions import *


class MovieRepository(Repository[Movie]):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Movie:
        target_movie = self.session.query(Movie).filter(Movie.id == id).first()        
        if target_movie == None :
            raise MovieNotFound
        return target_movie

    def get_all(self) -> List[Movie]:
        movies = self.session.query(Movie).all()
        return movies
    
    def add(self, **kwargs: object) -> Movie:
        pass
    
    def update(self, id: int, **kwargs: object) -> Movie:
        pass
    
    def delete(self, id: int) -> None:
        pass

    def filter(
        self,
        title: Optional[str] = None,
        release_year: Optional[int] = None,
        genre: Optional[str] = None,
    ) -> list[Movie]:
        query = self.session.query(Movie)
        if title:
            query = query.filter(Movie.title.like(f"%{title}%"))
        if release_year:
            query = query.filter(Movie.release_year == release_year)
        if genre:
            query = query.join(Movie.genres).filter(Genre.name == genre).distinct()

        return query.all()