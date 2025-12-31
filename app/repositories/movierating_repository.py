from .repository_schema import *

class MovieRatingRepository(Repository[MovieRating]):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> MovieRating:
        pass

    def get_all(self) -> List[MovieRating]:
        pass
    
    def add(self, **kwargs: object) -> MovieRating:
        pass
    
    def update(self, id: int, **kwargs: object) -> MovieRating:
        pass
    
    def delete(self, id: int) -> None:
        pass