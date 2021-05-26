
from my_list import List, T
from typing import Generic

class Node(Generic[T]):

    def __init__(self, item:T = None)-> None:
        self.item = item
        self.link = None

class LinkedListIterator(Generic[T]):

    def __init__(self, a_list:List[T])->None:
        self.list = a_list
        self.previous = None
        self.current = a_list.head


    def __iter__(self):
        return self

    def __next__(self):
        if self.current is not None:
            item = self.current.item
            self.previous = self.current
            self.current = self.current.link
            return item
        else:
            raise StopIteration

    def has_next(self):
        return self.current is not None

    def peek(self):
        try:
            return self.current.item
        except AttributeError:
            raise StopIteration("No more elements in list")


    def delete(self)->T:
        if not self.has_next():
            raise StopIteration("No more elements in list")
        else:
            item = self.current.item
            self.current = self.current.link
            if self.previous is None:
                self.list.head = self.current
            else:
                self.previous.link = self.current
            self.list.length-=1
            return item

    def reset(self):
        self.current = self.list.head

class LinkedList(List[T]):

    def __init__(self)->None:
        List.__init__(self)
        self.head = None

    def __iter__(self)->LinkedListIterator[T]:
        return LinkedListIterator(self)

    def __get_node_at_index(self, index: int) -> Node[T]:
        if 0 <= index and index < len(self):
            current = self.head

            for i in range(index):
                current = current.link
            return current
        else:
            raise ValueError("Index out of bounds")

    def __setitem__(self, index: int, item: T) -> None:
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item

    def delete_at_index(self, index: int) -> T:
        if not self.is_empty():
            if index > 0:
                previous_node = self.__get_node_at_index(index - 1)
                item = previous_node.link.item
                previous_node.link = previous_node.link.link
            elif index == 0:
                item = self.head.item
                self.head = self.head.link
            else:
                raise ValueError("Index out of bounds")
            self.length -= 1
            return item
        else:
            raise ValueError("Index out of bounds: list is empty")

    def insert(self, index: int, item: T) -> None:
        new_node = Node(item)

        if index > 0:
            previous_node = self.__get_node_at_index(index - 1)
            new_node.link = previous_node.link
            previous_node.link = new_node
        elif index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            raise ValueError("Index out of bounds")
        self.length += 1

    def index(self, item: T) -> int:
        current = self.head
        index = 0
        while current is not None and current.item != item:
            current = current.link
            index += 1
        if current is None:
            raise ValueError("Item is not in list")
        else:
            return index

    def delete_negative(self):
        """ delete all negative values in the list"""
        prev_node = self.head
        if prev_node is None:
            raise Exception("Empty List")
        cur_node = prev_node.link
        #start from second node
        while cur_node!=None:
            # print(cur_node.item)
            if cur_node.item<0:
                prev_node.link = cur_node.link
            else:
                prev_node = cur_node

            cur_node = cur_node.link

        #if the first item is negative, remove that as well
        if self.head.item<0:
            self.head = self.head.link

    def delete_negatives(self):
        prev_node = self.head

        for _ in range(self.length):
            cur_node = prev_node.link
            if cur_node.item <0:
                prev_node.link = cur_node.link
                self.length-=1
            else:
                prev_node = cur_node

        if self.length > 0  and self.head.item < 0:
            self.head = self.head.link
            self.length-=1


    def double(self):
        current = self.head
        for i in range(self.length):
            new_node = Node(current.item)
            new_node.link = current.link
            current.link = new_node
            current = new_node.link
        self.length*=2

    def print_list(self):
        cur = self.head
        while cur!=None:
            print(cur.item)
            cur = cur.link


def delete_negative(my_list:List[T])->None:
    """ delete all negative items in the given list"""
    it = iter(my_list)
    while it.has_next():
        if it.peek()<0:
             it.delete()
        else:
            next(it)

    # it.reset()





def print_repeating(a_list: List[T])->None:
    """  for each item in position k, prints the item k + 1 times """
    count = 0
    while count<len(a_list):
        for _ in range(count+1):
            print(a_list[count], end=",")
        count+=1


def max(a_list:List[T])->T:
    it = iter(a_list)
    try:
        max = next(it)
    except StopIteration:
        raise Exception("List is empty")
    else:
        for i in it:
            if max < i:
                max=i
        return max




# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(-13)
# my_list.append(4)
# my_list.append(5)
#
#
# l = delete_negative(my_list)
# my_list. print_list()
#
# # it = iter(my_list)
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# #
# # print(it.has_next())
# # print(next(it))
# my_list.print_list()

