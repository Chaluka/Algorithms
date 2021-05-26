
from my_queue import Queue, T
from referential_array import ArrayR

class LinearQueue(Queue[T]):

    MIN_CAPACITY = 1

    def __init__(self, max_capacity:int)->None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(LinearQueue.MIN_CAPACITY, max_capacity))

    def clear(self)->None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0

    def is_full(self) ->bool:
        return self.rear == len(self.array)

    def append(self,item:T) ->None:
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear += 1

    def serve(self) ->T:
        if self.is_empty():
            raise Exception("Queue is empty")

        self.front += 1
        self.length -= 1
        return self.array[self.front-1]
