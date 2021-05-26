

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
class Queue(ABC,Generic[T]):

    def __init__(self)->None:
        self.length = 0

    @abstractmethod
    def append(self,item:T)->None:
        pass

    @abstractmethod
    def serve(self)->T:
        pass

    def __len__(self)->int:
        return self.length

    def is_empty(self):
        return len(self)==0

    @abstractmethod
    def is_full(self)->bool:
        pass
    