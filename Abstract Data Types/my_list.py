
"""
    List ADT Implementation - This is the abstract class of the List.
    This is the base class for both ArrayList and LinkedList classes.

    This class gives an interface for all the derived classes. The functions 
    setitem/getitem,insert/delete_at_index/get_index are abstract methods which are implemented differently 
    in derived classes.
"""


__author__ = "Chaluka Salgado"
__copyright__ = "Copyright 2020 @ Kamikaze"
__email__ = "chaluka.salgado@gmail.com"
__date__ = "7-May-2020"
__updated__ = "27-Jun-2021"
__version__ = "1.0"

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from referential_array import ArrayR

T = TypeVar('T')

class List(ABC,Generic[T]):

    def __init__(self)->None:
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    def append(self, item: T) -> None:
        self.insert(len(self),item)

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        pass

    def remove(self, item:T)->None:
        """
            Remove the given item from the list. First it find the index of the given item 
            and then it deletes it using delete_at_index method.
        """
        index = self.index(item)
        self.delete_at_index(index)

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self)==0

    def clear(self):
        self.length = 0

