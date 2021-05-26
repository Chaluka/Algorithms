
from my_list import List, T
from referential_array import ArrayR

class ArrayList(List[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_capacity:int)->None:
        List.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY,max_capacity))


    def __getitem__(self, index:int)->T:
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        self.array[index] = value

    def index(self, item: T) -> int:
        for i in range(len(self)):
            if item == self.array[i]:
                return i

        raise ValueError("item not in list")

    def delete_at_index(self, index: int) -> T:
        item = self.array[index]
        self.length -= 1
        for i in range(index, self.length):
            self.array[i] = self.array[i + 1]



    def __newsize(self):
        return 2*len(self)

    def insert(self, index:int, item:T)->None:
        if len(self) == len(self.array):
            new_array = ArrayR(self.__newsize())
            for i in range(len(self)):
                new_array[i] = self.array[i]
            self.array = new_array
        self.length += 1
        for i in range(len(self)-1, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = item

    def __str__(self):
        lst_str = "[" + str(self.array[0])
        for i in range(1,len(self)):
              lst_str += "," +str(self.array[i])

        return lst_str + "]"