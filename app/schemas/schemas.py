from pydantic import BaseModel, Field
from typing import List, Optional


class MovieSchema(BaseModel):
    title: str = Field(..., min_length=1, example="Inception")
    director_id: int = Field(..., example=1)
    release_year: Optional[int] = Field(None, ge=1888, example=2010)
    cast: Optional[str] = Field(
        None,
        example="Leonardo DiCaprio, Joseph Gordon-Levitt"
    )
    genres: List[int] = Field(
        ...,
        min_items=1,
        example=[1, 3, 5]
    )