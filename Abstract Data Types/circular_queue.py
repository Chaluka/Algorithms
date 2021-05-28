
from my_queue import Queue, T
from referential_array import ArrayR

class CircularQueue(Queue[T]):
    """
        This is a variant of queue implemenatations called circular queue. The difference between 
        this and a normal queue is the front and rear ends move in circular manner. Basically, 
        the rear end connected back to the front end making a circle. Hence, the rear end can appear 
        before the front end in the flat queue and vice versa. This structure utilize the memory by 
        this circular movements of the two ends. 
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity:int)->None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def clear(self)->None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0

    def is_full(self) ->bool:
        return len(self) == len(self.array)

    def append(self,item:T) ->None:
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        # use modular (%) to pount the rear pointer back to position 0 after the last (nth) position
        self.rear = (self.rear +1) % len(self.array)

    def serve(self) ->T:
        if self.is_empty():
            raise Exception("Queue is empty")

        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        self.length -= 1
        return item

    def print_items(self)->None:
        index = self.front
        for _ in range(len(self)):
            print(self.array[index])
            index = (index+1) % len(self.array)

    def print_reverse_queue(self)->None:
        index = self.rear-1
        for _ in range(len(self)):
            print(self.array[index])
            index = (index - 1) % len(self.array)
