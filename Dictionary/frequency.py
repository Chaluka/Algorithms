

from enum import Enum
from hash_table import LinearProbeHashTable, T
from dictionary import Dictionary
from typing import TypeVar, Generic, Tuple, List
import string
from list import ArrayList
from referential_array import ArrayR
import sys

class Rarity(Enum):
    COMMON = 1
    RARE = 0
    UNCOMMON = 2
    MISSPELT = -1


class Frequency:

    DEFAULT_BVALUE = 250726
    DEFAULT_TABEL_SIZE = 1000081
    DEFAULT_FILENAME = 'english_large.txt'

    def __init__(self)->None:
        self.hash_table = LinearProbeHashTable()
        self.dictionary = Dictionary(self.DEFAULT_BVALUE, self.DEFAULT_TABEL_SIZE)
        self.dictionary.load_dictionary(self.DEFAULT_FILENAME)
        self.max_word:Tuple[int,int] = (0,0) # (word,freq)

    def __extract_words(self, line:str)->List[str]:
        """ This filters all the unnecessary attachments (specified in DELIMITERS) in the given line.
            And returns a list of words in the line
        """
        for punc in string.punctuation.remove('\''):
            line = line.replace(punc, '')

        return line.split(' ')


    def add_file(self, filename:str)->None:

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                #filter all delimiters and extract the words in the line
                # words = self.__extract_words(line.strip())
                words = line.strip(string.punctuation)
                # words = line.strip(string.punctuation).split(' ')
                words = [word.lower() for word in words if word!=""]
                for word in words:
                    #check whether word in the dictionary
                    if self.dictionary.find_word(word):
                        if word in self.hash_table:
                            # if already in the dictionary then increase the frequency
                            freq = self.hash_table[word] +1
                            self.hash_table[word] = freq
                            if self.max_word[1] < freq:
                                self.max_word = (word,freq)
                        else:
                            self.hash_table[word] = 1
                        # print(self.hash_table[word])

    def rarity(self, word:str)->Rarity:
        freq = self.hash_table[word]
        if  freq >= self.max_word[1]/100:
            return Rarity.COMMON
        elif freq < self.max_word[1]/1000:
            return Rarity.RARE
        elif freq < self.max_word[1]/100 and freq >= self.max_word[1]/1000:
            return Rarity.UNCOMMON
        else:
            return Rarity.MISSPELT

    def __swap(self, array: ArrayR, index1: int, index2: int)->None:
        """ swap the elements corresponds to the given indices"""
        array[index1], array[index2] = array[index2], array[index1]


    def __partition(self,array: ArrayR, start: int, end: int) -> int:
        mid = (start + end) // 2

        pivot = array[mid][1]
        self.__swap(array, start, mid)
        boundary = start
        for k in range(start + 1, end + 1):
            if array[k][1] > pivot:
                boundary += 1
                self.__swap(array, k, boundary)

        self.__swap(array, start, boundary)
        return boundary

    def quick_sort(self, array: ArrayR) -> None:
        start = 0

        end = len(array) - 1
        self.__quick_sort_aux(array, start, end)

    def __quick_sort_aux(self,array: ArrayR, start: int, end: int) -> None:
        if start < end:
            boundary = self.__partition(array, start, end)

            self.__quick_sort_aux(array, start, boundary - 1)
            self.__quick_sort_aux(array, boundary + 1, end)

    def ranking(self) -> ArrayList[Tuple]:
        """ rank the words in descending order based on their frequencies"""
        rank_lst = ArrayList(len(self.hash_table))
        for item in self.hash_table:
            if item is not None:
                rank_lst.append(item)

        self.quick_sort(rank_lst)
        return rank_lst


def get_user_input(max_limit:int)->int:
    """ get number of words from the user"""
    while True:
        try:
            num_words = int(input("Number of words : "))
            if num_words>0 and num_words<=max_limit:
                return num_words
            raise ValueError
        except ValueError:
            print("Invalid Input..!! (0 < value <= {})".format(max_limit))

def frequency_analysis() -> None:
    file_lst = ['215-0.txt','84-0.txt', '1342-0.txt', '2600-0.txt', '98-0.txt']
    f = Frequency()
    f.add_file(file_lst[0])
    max_words = len(f.dictionary)
    #user must input a number which is less than the words in the dictionary
    num_wrods = get_user_input(max_words)

    while True:
        try:
            rank_lst = f.ranking()
        except RecursionError:
            print("RecursionError: maximum recursion depth exceeded.")
            rec_depth = sys.getrecursionlimit()
            sys.setrecursionlimit(rec_depth * 10)
            print("Recursion depth has been increased. Re-running the ranking method\n")
        else:
            break

    print("Rank\tWord\tFrequency\tRarity")
    for i in range(num_wrods):
        word, freq = rank_lst[i]
        print("{}\t\t{}\t\t{}\t\t{} ".format(i+1, word, freq, f.rarity(word)))


if __name__ == "__main__":

    frequency_analysis()








