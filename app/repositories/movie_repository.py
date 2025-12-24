from repository_schema import *

class MovieRepository(Repository[Movie]):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Movie:
        pass

    def get_all(self) -> List[Movie]:
        pass
    
    def add(self, **kwargs: object) -> Movie:
        pass
    
    def update(self, id: int, **kwargs: object) -> Movie:
        pass
    
    def delete(self, id: int) -> None:
        pass