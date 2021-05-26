
from typing import TypeVar
from stack import Stack, T
from linked_list import Node


class LinkedStack(Stack[T]):

    def __init__(self):
        Stack.__init__(self)
        self.top = None

    def is_full(self) ->bool:
        return False

    def clear(self) ->None:
        Stack.clear(self)
        self.top = None

    def push(self, item:T) ->None:
        new_node = Node(item)
        new_node.link = self.top
        self.top = new_node
        self.length+=1

    def pop(self) ->T:
        if not self.is_empty():
            item = self.top.item
            self.top = self.top.link
            self.length-=1
            return item
        else:
            raise ValueError("Stack is empty")

    def peek(self) ->T:
        return self.top.item

    def sum_all(self) -> int:
        current = self.top
        sum = 0
        while current is not None:
            sum += current.item
            current = current.link

        return sum



def serve(self):
    while not self.rear_stack.is_empty():
        self.front_stack.push(self.rear_stack.pop())

    if not self.front_stack.is_empty():
        return self.front_stack.pop()
    else:
        raise Exception("Queue is empty")



if __name__=="__main__":
    s = LinkedStack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

print(s.sum_all())