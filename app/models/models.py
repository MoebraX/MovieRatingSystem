from sqlalchemy import *
from sqlalchemy.orm import relationship

from app.db.base import Base


movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key = True),
    Column("genre_id", ForeignKey("genres.id"), primary_key = True),
)


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    birth_year = Column(Integer)
    description = Column(Text)

    movies = relationship("Movie", back_populates="director")

    def __init__(self, name: str, birth_year: int | None = None, description: str | None = None):
        self.name = name
        self.birth_year = birth_year
        self.description = description


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    release_year = Column(Integer)
    cast = Column(Text)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable = False)
    director = relationship("Director", back_populates = "movies")
    genres = relationship("Genre", secondary = movie_genres, back_populates = "movies")
    ratings = relationship("MovieRating", back_populates = "movie", cascade = "all, delete-orphan")

    def __init__(
        self,
        title: str,
        director_id: int,
        release_year: int | None = None,
        cast: str | None = None,
    ):
        self.title = title
        self.director_id = director_id
        self.release_year = release_year
        self.cast = cast


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)
    description = Column(Text)
    movies = relationship("Movie", secondary = movie_genres, back_populates = "genres")

    def __init__(self, name: str, description: str | None = None):
        self.name = name
        self.description = description


class MovieRating(Base):
    __tablename__ = "movie_ratings"

    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable = False)
    score = Column(Integer, nullable = False)
    movie = relationship("Movie", back_populates = "ratings")

    __table_args__ = (
        CheckConstraint("score >= 1 AND score <= 10", name = "check_score_range"),
    )

    def __init__(self, movie_id: int, score: int):
        if not 1 <= score <= 10:
            raise ValueError("Score must be between 1 and 10")
        self.movie_id = movie_id
        self.score = score