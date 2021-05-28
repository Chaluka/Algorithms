

from stack import Stack,T
from referential_array import ArrayR

class ArrayStack(Stack[T]):
    """ An array implementation of stack. This uses an array to store the elements and 
        push/pop operations are done using direct addressing with the help of a pointer points 
        to the top of the stack.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity:int)->None:
        Stack.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def is_full(self) ->bool:
        """ 
            Returns a bool value (True or False) implying whether stack is empty or not.
        """
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        """ 
            Push the given item (T) onto the stack

        Raises:
            Exception: when the stack is full
        """
        if self.is_full():
            raise Exception("Stack is full")

        self.array[len(self)] = item
        self.length+=1

    def pop(self) ->T:
        """
            Remove the item at the top of the stack and return it

        Raises:
            Exception: when the stack is empty

        """
        if self.is_empty():
            raise Exception("Stack is empty")

        self.length-=1
        return self.array[self.length]

    def peek(self) ->T:
        """
            Return the value of item at the top of the stack without removing it

        Raises:
            Exception: when the stack is empty

        """
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.array[len(self)-1]
