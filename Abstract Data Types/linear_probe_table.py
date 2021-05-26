from my_referential_array import ArrayR
import copy
from sympy import isprime
from typing import TypeVar, Generic
T = TypeVar('T')

class LinearProbeTable(Generic[T]):

    LOAD_FACTOR = 2/3

    def __init__(self, size:int= 7919)->None:
        self.count = 0
        self.table = ArrayR(size)

    def __len__(self)->int:
        return self.count

    def __get_new_size(self, size):
        size *=2
        while not isprime(size):
            size+=1
        return size

    def rehash(self):
        load_factor = self.count/len(self.table)
        if load_factor >= self.LOAD_FACTOR:
            # print("rehashing as load factor exceeds")
            old_table = copy.copy(self.table)
            #resize the table
            self.table = ArrayR(self.__get_new_size(len(self.table)))
            self.count=0
            #rehash all the values to new table
            for item in old_table:
                key, value = item
                self.__setitem__(key,value)

    def hash(self,key:str)->int:
        value = 0
        a = 31415
        b = 27183
        for char in key:
            value = (ord(char) + a*value) % len(self.table)
            a = a*b % (len(self.table)-1)
        return value

    def __setitem__(self, key: str, value: T):
        # print("insert {}".format(key))
        try:
            position = self.__linear_probe(key,False)
        except KeyError:
            self.rehash()
            self.__setitem__(key,value)
        else:
            if self.table[position] is None:
                self.count+=1
            self.table[position] = (key,value)

    def __getitem__(self, key:str)->T:
        position = self.__linear_probe(key, True)
        return self.table[position]

    def __linear_probe(self,key: str, is_search: bool)->int:
        position = self.hash(key)
        for _ in range(len(self.table)):
            if self.table[position] is None:
                if is_search:
                    raise KeyError(key)
                else:
                    return position
            elif self.table[position][0] == key:
                return position
            else:
                position = (position+1)% len(self.table)
        #at this point, we have gone through the table and key not found
        raise KeyError(key)

    def __str__(self):
        result = ""
        for item in self.table:
            if item is not None:
                key, value = item
                result += "({}, {})".format(str(key),str(value))
        return result

    def __delitem__(self, key: str) -> None:
        pos = self.__linear_probe(key, False)
        self.table[pos] = None
        self.count -= 1

        pos = (pos + 1) % len(self.table)
        while self.table[pos] is not None:
            item = self.table[pos]
            self.table[pos] = None
            self[str(item[0])] = item[1]
            pos = (pos + 1) % len(self.table)



hash_table = LinearProbeTable(7)
hash_table['Aho'] = 0
hash_table['Kruse'] = 5
hash_table['Standish'] = 1
hash_table['Horowitz'] = 5
hash_table['Langsam'] = 5
hash_table['Sedgewick'] = 2
hash_table['Knuth'] = 1
hash_table['Knuthi'] = 1

del hash_table['Knuth']

print(hash_table)

print(len(hash_table.table))
