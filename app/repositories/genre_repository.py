from .repository_schema import *

class GenreRepository(Repository[Genre]):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Genre:
        target_genre = self.session.query(Genre).filter(Genre.id == id).first()        
        if target_genre == None :
            raise GenreNotFound
        return target_genre

    def get_all(self) -> List[Genre]:
        pass
    
    def add(self, **kwargs: object) -> Genre:
        pass
    
    def update(self, id: int, **kwargs: object) -> Genre:
        pass
    
    def delete(self, id: int) -> None:
        pass