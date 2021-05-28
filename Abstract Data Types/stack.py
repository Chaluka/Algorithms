"""
    Stack ADT Implementation - This is the abstract class of the Stack.
    This is the base class for both ArrayStack and LinkedStack

    This class gives an interface for all the derived classes. The functions 
    push/pop/peek/is_full are abstract methods which are implemented differently 
    in derived classes.
"""


__author__ = "Chaluka Salgado"
__copyright__ = "Copyright 2020 @ Kamikaze"
__email__ = "chaluka.salgado@gmail.com"
__date__ = "01-May-2020"
__updated__ = "27-Jun-2021"
__version__ = "1.0"


from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

class Stack(ABC, Generic[T]):
    """ 
        Generic[T] as a base class defines that the class Stack takes a single type parameter T .
        This also makes T valid as a type within the class body. Moreover, Stack[T] is also valid as a type.
    """
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

