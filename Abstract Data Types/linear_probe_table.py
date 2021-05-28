""" 
    This is a hash table (or a look up table) implemetation that maintains a 
    collection of key-values pairs. The values are associated with the keys. 
    Each of these key-value pairs are stored based on generated key called hash 
    key. This hash key is generated with respect to the given key. The following 
    are the important features that you must be aware of before importing this module.
    
    Probing - linear probing is used to resolve the collisions in the table.
    Load Factor - number of elements in the table/ total size of the table
    Rehashing - when the number of elements exceeds the load factor 
                (its 2/3 in this implementation), table size is doubled 
                and all values are rehashed.
     



"""

__author__ = "Chaluka Salgado"
__copyright__ = "Copyright 2020 @ Kamikaze"
__email__ = "chaluka.salgado@gmail.com"
__date__ = "7-May-2020"
__updated__ = "27-Jun-2021"
__version__ = "1.0"

from referential_array import ArrayR
import copy
from sympy import isprime
from typing import TypeVar, Generic
T = TypeVar('T')


class LinearProbeTable(Generic[T]):

    LOAD_FACTOR = 2/3

    def __init__(self, size: int = 7919) -> None:
        self.count = 0
        self.table = ArrayR(size)

    def __len__(self) -> int:
        return self.count

    def __get_new_size(self, size):
        """ 
            Return a new size which is the closes prime number to the doubled value of the given size
        """
        size *= 2
        while not isprime(size):
            size += 1
        return size

    def rehash(self):
        """ 
            Create a new double sized table and insert (hash) all elements back into new table.    
        """
        load_factor = self.count/len(self.table)
        if load_factor >= self.LOAD_FACTOR:
            # print("rehashing as load factor exceeds")
            old_table = copy.copy(self.table)
            # resize the table
            self.table = ArrayR(self.__get_new_size(len(self.table)))
            self.count = 0
            # rehash all the values to new table
            for item in old_table:
                key, value = item
                self.__setitem__(key, value)

    def hash(self, key: str) -> int:
        """
            Return a hash key generated with respect to the given key. A Polynomial rolling 
            approach is used to generate the hash key. (This is a universal hash function for strings)

            hash(str) = str[0].a^0 + str[1].a^1 + str[2].a^2 + .... + str[n].a^n

        Args:
            key (str): key is passed as a string
        """
        value = 0
        a = 31415
        b = 27183
        for char in key:
            value = (ord(char) + a*value) % len(self.table)
            a = a*b % (len(self.table)-1)
        return value

    def __setitem__(self, key: str, value: T):
        """
            Insert an item into the hash table based on it's hash key. 
            In key-value pair, 
                key must be a string and 
                value could be any data type

        """
        try:
            position = self.__linear_probe(key, False)
        except KeyError:
            self.rehash()
            self.__setitem__(key, value)
        else:
            if self.table[position] is None:
                self.count += 1
            self.table[position] = (key, value)

    def __getitem__(self, key: str) -> T:
        """ 
            Retrurn key-value pair with respect to the given key
        """
        position = self.__linear_probe(key, True)
        return self.table[position]

    def __linear_probe(self, key: str, is_search: bool) -> int:
        """ 
            When hashed key mapped into a already occupied cell of the hash
            table, linear probe search for the next available/possible posistion 
            for the given key in insertion/retrieval respectively.
        """
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
                position = (position+1) % len(self.table)
        # at this point, we have gone through the table and key not found
        raise KeyError(key)

    def __str__(self):
        result = ""
        for item in self.table:
            if item is not None:
                key, value = item
                result += "({}, {})".format(str(key), str(value))
        return result

    def __delitem__(self, key: str) -> None:
        """ 
            Delete a key-value pair w.r.t the given key. A deletion of an element 
            at nth position is required rehash all elements from (n+1)th item until 
            a empty cell is found. 

        """
        pos = self.__linear_probe(key, False)
        self.table[pos] = None
        self.count -= 1

        pos = (pos + 1) % len(self.table)
        while self.table[pos] is not None:
            item = self.table[pos]
            self.table[pos] = None
            self[str(item[0])] = item[1]
            pos = (pos + 1) % len(self.table)


if __name__ == "__main__":
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
