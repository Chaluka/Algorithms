"""
The file trie.py contains the implementation of tries

"""

__author__ = "Chaluka Salgado"
__copyright__ = "Copyright 2020, FIT2004 Teaching Materials"
__email__ = "chaluka.salgado@gmail.com"
__docformat__ = 'reStructuredText'


class Node:
    ARRAY_SIZE = 27

    def __init__(self) -> None:
        self.array = [None] * self.ARRAY_SIZE
        self.char = ''
        self.count = 0
        self.strings = []

    def char_to_int(self, char: chr) -> int:
        if ord(char) == 36:  # when char is $ sign
            return 26
        int_value = ord(char)
        # if int_value > 90:
        #     int_value-= 32
        return (int_value - 97)

    def insert(self, char: chr, str_ind: int) -> None:
        node = Node()
        print("INSERT : {}".format(char))
        self.array[self.char_to_int(char)] = node
        node.char = char
        node.count += 1
        node.strings.append(str_ind)
        return node

    def insert_str(self, in_str: str, index: int, str_ind: int) -> bool:

        if len(in_str) - 1 < index:  # This will return True after all characters have been inserted
            return True

        print("At Node {}. Inserting string[{}]={}".format(self.char, index, in_str[index]))
        char = in_str[index]
        node = self.array[self.char_to_int(char)]
        if node == None:
            node = self.insert(char, str_ind)
        else:
            node.count += 1
            node.strings.append(str_ind)

        node.insert_str(in_str, index + 1, str_ind)

    def find(self, char: chr):
        index = self.char_to_int(char)
        return self.array[index]

    def find_str(self, string: str, index: int) -> bool:
        node = self.find(string[index])
        if index == len(string) - 1:
            if node != None:
                return True, node.count, node.strings
            else:
                return False, 0, []
        else:
            if node == None:
                return False, 0, []
            else:
                return node.find_str(string, index + 1)


class Trie:

    def __init__(self) -> None:
        self.root = None
        self.string_list = []
        self.size = 0

    def insert(self, string: str, index=0) -> None:
        self.string_list.append(string)

        if self.root == None:
            self.root = Node()
            self.root.char = "root"

        self.root.insert_str(string, index, self.size)
        self.size += 1

    def find_str(self, string: str):
        found, count, str_lst = self.root.find_str(string, 0)
        out_lst = [self.string_list[index][:-1] for index in str_lst]

        return count, out_lst

    def wildcard_prefix_freq(self, query_str: str):
        wildcard_index = 0
        for i in range(len(query_str)):
            if query_str[i] == '?':
                wildcard_index = i
        total_count = 0
        strings = []
        for i in range(26):
            query_str = query_str[:wildcard_index] + chr(i + 97) + query_str[wildcard_index + 1:]
            _, count, str_lst = self.root.find_str(query_str, 0)
            total_count += count
            strings.extend(str_lst)

        return total_count, [self.string_list[index][:-1] for index in strings]


class SuffixTrie(Trie):

    def __init__(self):
        Trie.__init__(self)

    def build_suffix_trie(self, string: str):
        n = len(string)
        for i in range(n):
            self.insert(string, i)
            print("---------------")


trie = Trie()
suffix_trie = SuffixTrie()
str_lst = ['aa', 'aab', 'aaab', 'abaa', 'aa', 'abba', 'aaba', 'aaa', 'aa', 'aaab', 'abbb', 'baaa', 'baa', 'bba', 'bbab']

# trie.insert("ABCD$")
for str1 in str_lst:
    str1 += "$"
    print("\n Insert {} to trie".format(str1))
    trie.insert(str1)

print("\n\nFind the prefix frequency")
print(trie.find_str('aa'))
print("\n\nFind the wildcard prefix")
y = trie.wildcard_prefix_freq('a?a')
print(y)
