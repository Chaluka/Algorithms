"""
Stack ADT Implementation
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

class Stack(ABC, Generic[T]):
    #Generic[T] as a base class defines that the class Stack takes a single type parameter T .
    # This also makes T valid as a type within the class body. Moreover, Stack[T] is also valid as a type.

    def __init__(self)->None:
        self.length = 0
    @abstractmethod
    def push(self, item:T)->None:
        pass

    @abstractmethod
    def pop(self)->T:
        pass

    @abstractmethod
    def peek(self)->T:
        pass

    def __len__(self)->int:
        return self.length

    def is_empty(self)->bool:
        return len(self)==0

    @abstractmethod
    def is_full(self)->bool:
        pass

    def clear(self)->None:
        self.length = 0





def func(s: Stack[T]):
    return s