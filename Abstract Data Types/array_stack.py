

from stack import Stack,T
from referential_array import ArrayR

class ArrayStack(Stack[T]):

    MIN_CAPACITY = 1

    def __init__(self, max_capacity:int)->None:
        Stack.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def is_full(self) ->bool:
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        if self.is_full():
            raise Exception("Stack is full")

        self.array[len(self)] = item
        self.length+=1

    def pop(self) ->T:
        if self.is_empty():
            raise Exception("Stack is empty")

        self.length-=1
        print(self.array[self.length])
        return self.array[self.length]

    def peek(self) ->T:
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.array[len(self)-1]
