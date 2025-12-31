from .repository_schema import *

class DirectorRepository(Repository[Director]):
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Director:
        pass

    def get_all(self) -> List[Director]:
        pass
    
    def add(self, **kwargs: object) -> Director:
        pass
    
    def update(self, id: int, **kwargs: object) -> Director:
        pass
    
    def delete(self, id: int) -> None:
        pass