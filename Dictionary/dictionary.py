"""
This file contains the implementation for FIT2085 Interview Prac 3
Following concepts are used,
    - Hash Tables
    -


"""

__author__ = "Chaluka Salgado"
__docformat__ = 'reStructuredText'


from hash_table import LinearProbeHashTable
import io
import os
import timeit
from typing import TypeVar,Tuple

class Dictionary:

    def __init__(self, hash_base: int, table_size: int) -> None:
        self.hash_table = LinearProbeHashTable(hash_base,table_size)

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """ read words into the dictionary with integer 1 as the associated data
            from the given file"""
        word_counter = 0
        with open(filename,"r",encoding="utf-8") as file:
            start_time = timeit.default_timer()
            for line in file:
                word = line.strip()
                self.hash_table.insert(word,1)
                word_counter+=1
                current_time = timeit.default_timer() - start_time
                if time_limit is not None and current_time >=time_limit:
                    raise TimeoutError("File read time exceeded")
        return word_counter


    def add_word(self, word:str)->None:
        """ adds the given word to the dictionary with integer 1 as the associated data"""
        self.hash_table.insert(word.lower(),1)

    def find_word(self, word: str) -> bool:
        """ returns true if the word is in the dictionary"""
        return word.lower() in self.hash_table

    def delete_word(self, word: str) -> None:
        """ deletes the given word from the dictionary"""
        del self.hash_table[word.lower()]

    def __str__(self):
        return str(self.hash_table)

    def __len__(self):
        return len(self.hash_table)

    def menu(self)->None:
        """ display the following menu and allows user to interact with the dictionary
            1 . Read File
            2 . Add Word
            3 . Find Word
            4 . Delete Word
            5 . Exi t
        :raises: ValueError exception if the user enter an invalid input

        """
        input_flag = True
        while input_flag:
            break_line = '_' * 30
            print(break_line)
            print("1. Read File")
            print("2. Add Word")
            print("3. Find Word")
            print("4. Delete Word")
            print("5. Exit")
            print(break_line)
            try:
                option = input("Enter option : ")
                option = int(option)
                if option > 5:
                    raise ValueError
            except ValueError:
                print("Invalid option..!! Try again.")
            else:
                if option==1:
                    filename = input("Enter file name (e.g., example.txt): ")
                    try:
                        self.load_dictionary(filename)
                    except FileNotFoundError:
                        print("File [{}] not found in the directory".format(filename))
                    else:
                        print("Successfully read file")
                elif option==2:
                    word = input("Enter word : ")
                    self.add_word(word)
                    print("[{}] Successfully added".format(word))
                elif option==3:
                    word = input("Enter word : ")
                    found = self.find_word(word)
                    if found:
                        print("[{}] Found in dictionary".format(word))
                    else:
                        print("[{}] Not found in dictionary".format(word))
                elif option==4:
                    try:
                        word = input("Enter word : ")
                        self.delete_word(word)
                    except KeyError:
                        print("[{}] Not found in dictionary".format(word))
                    else:
                         print("[{}] Deleted from dictionary".format(word))
                else:
                    input_flag = False

class Statistics:
    FILENAMES = ['english_small.txt', 'english_large.txt', 'french.txt']
    B_VALUES = [1, 27183, 250726]
    TABLE_SIZES = [250727, 402221, 1000081]

    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> Tuple:
        """  creates a new dictionary with hash_base and table_size,
            and returns the tuple (words, time, collision_count, probe_total, probe_max, rehash_count)"""
        dic = Dictionary(hash_base,table_size)
        time_spent = 0
        try:
            start = timeit.default_timer()
            dic.load_dictionary(filename,max_time)
            time_spent = timeit.default_timer()-start
        except TimeoutError:
            c, p, m, r = dic.hash_table.statistics()
            return len(dic.hash_table), max_time, c, p, m, r
        else:
            c, p, m, r = dic.hash_table.statistics()
            return len(dic.hash_table), time_spent, c, p, m, r


    def table_load_statistics(self, max_time) -> None:
        """ create dictionaries for a given set of files and write statistics into a csv file"""

        out_filename = "output task2.csv"
        if os.path.isfile(out_filename):  # if the file already exists, remove it.
            os.remove(out_filename)

        file = open(out_filename, "w")
        #writing header into the csv file
        file.write("Hash Base,Table Size,Label,Filename,Words,Time,Collisions,Probes,Probe Max,Rehash\n")
        for base in self.B_VALUES:
            for table_size in self.TABLE_SIZES:
                flag = True
                for filename in self.FILENAMES:
                    w, t, c, p, m, r = self.load_statistics(base,table_size,filename, max_time)
                    #Hash Base | Table Size | Label | Filename | Words | Time | Collisions | Probes | Probe Max | Rehash
                    if flag:
                        file.write("{},{},B={} / TS = {},{},{},{},{},{},{},{}\n".format(base,table_size,base,table_size,filename,w,t,c,p,m,r))
                        flag = False
                    else:
                        file.write("{},{}, ,{},{},{},{},{},{},{}\n".format(base, table_size, filename, w, t, c, p, m, r))

        file.close()

        assert os.path.isfile(filename), "output file has not been created"




if __name__=="__main__":
    # stat = Statistics()
    # start = timeit.default_timer()
    # stat.table_load_statistics(10)
    # end = timeit.default_timer() - start
    # print(end)
    dic = Dictionary(250726,1000081)
    dic.load_dictionary('english_large.txt')
    print(dic.find_word('a'))