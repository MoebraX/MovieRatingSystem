from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from sqlalchemy import *
from sqlalchemy.orm import joinedload
from datetime import *

from app.db.session import *
from app.models.models import *
from app.exceptions.repository_exceptions import *


T = TypeVar("T")
class Repository(ABC, Generic[T]):
    @abstractmethod
    def get(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError
    
    @abstractmethod
    def add(self, **kwargs: object) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: int, **kwargs: object) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError