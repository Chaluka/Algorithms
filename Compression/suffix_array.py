

from typing import List, Tuple, TypeVar
from copy import deepcopy

T = Tuple[int,int]


class SuffixArray:
    DOMAIN_SIZE = 27
    BASE_VALUE = ord('A') -1 #we need to map $ sign into 0th index
    END_CHAR = '$'

    def __init__(self)->None:
        self.string = None
        self.length = None
        self.rank_array = None

    def __get_int_value(self,char:chr)->int:
        """ This return the index of a given character
            '$' maps to index 0 and 'A' maps to index 1 and so on
        """
        if ord(char)==ord(self.END_CHAR):
            return 0

        return int(ord(char)-self.BASE_VALUE)

    def __sort_first_char(self, string:str)->List[int]:
        """ This will rank the suffixes based on first character.
            Its's required the ord value of the characters to rank them
            e.g., ord('A') = 65
        """
        count_array = [[] for i in range(self.DOMAIN_SIZE)]
        length = len(string)
        for i in range(length):
            count_array[self.__get_int_value(string[i])].append(i)

        count = 0
        out_lst = []
        for i in range(self.DOMAIN_SIZE):
            if len(count_array[i])!=0:
                count+=1
            for index in count_array[i]:
                out_lst.append((index,count))

        return out_lst

    def map_to_rank_array(self, lst:List[T])->None:
        """ This maps the given list of (id,rank) to corresponding indices in self.rank_array  """
        for i in range(len(lst)):
            id, rank = lst[i]
            self.rank_array[id] = rank

    def counting_sort(self, lst:List[T])->List[T]:
        """ This sort tuples based on the rank values tagged along with them
            :param lst: a list of tuples where each tuple (suffix id, rank)
        """
        length = max(lst, key= lambda item:item[1])[1]
        out_lst = []
        count_array = [[] for i in range(length+1)]
        for i in lst:
            id, rank = i
            count_array[rank].append(id)

        count=0
        for i in range(length+1):
            if len(count_array[i])>0:
                count+=1
            for id in count_array[i]:
                out_lst.append((id,i))

        return out_lst


    def build_suffix_array(self, string:str)->List[T]:
        """
            This constructs the suffix array for the given string using prefix doubling.
        :param string:
        :return: a list of tuples where each tuple is (suffix id, rank)
        :complexity: Worst case is O(N.log^2 N)
        """

        #Initialize instance variables
        self.string = string
        self.length = len(string)
        self.rank_array = [None]*self.length

        #first sort all the suffixes based on first character
        #here we use counting sort with there ord values - O(N)
        sorted_rank_array = deepcopy(self.__sort_first_char(string))
        self.map_to_rank_array(sorted_rank_array)

        #next onwards we sort based on next 2^k characters
        #this gives us O(nlog^2(n)) complexity
        k = 1
        sorted_flag = False
        while k<=self.length:
            # Invariant: suffix array has been sort based first 2^(k-1) characters
            sorted_flag = True
            slice_list = [0]
            temp_sorted_rank_array=deepcopy(sorted_rank_array)
            #create a sorted copy of the rank array
            for i in range(1,len(sorted_rank_array)):
                prev_id, prev_rank = temp_sorted_rank_array[i-1]
                cur_id, cur_rank = temp_sorted_rank_array[i]

                #if both have same rank then we need to get the rank cased on next k characters
                #so we replace the rank with new rank
                if prev_rank == cur_rank:
                    """ If same ranks we looking at ranks of suffix[k:n]"""
                    sorted_rank_array[i-1] = (prev_id, self.rank_array[prev_id+k])
                    sorted_rank_array[i] = (cur_id,self.rank_array[cur_id+k])
                    sorted_flag = False

                else:
                    """ If different then we change the rank values to negatives. Becuase, later (i.e., after sorting the slices) we can differentiate them with new ranks"""
                    if i==1:
                        sorted_rank_array[i - 1] = (prev_id, prev_rank*-1)
                    sorted_rank_array[i] = (cur_id, cur_rank*-1)
                    slice_list.append(i)
            # length of the list is the end of the last slice, so append it
            slice_list.append(len(sorted_rank_array))

            """ slices have the same rank, thus we need to sort them further based on first k characters"""
            for i in range(len(slice_list)-1):
                start = slice_list[i]
                end = slice_list[i+1]
                if (end-start)>1:
                    out = self.counting_sort(sorted_rank_array[start:end])
                    for i in out:
                        sorted_rank_array[start]=i
                        start+=1

            temp_sorted_rank_array = deepcopy(sorted_rank_array)

            """ after sorting we revisit the array to update the ranks"""
            count = 0
            sorted_rank_array[0] = (sorted_rank_array[0][0], count)
            for i in range(1, len(sorted_rank_array)):
                prev_id, prev_rank = temp_sorted_rank_array[i - 1]
                cur_id, cur_rank = temp_sorted_rank_array[i]
                if prev_rank!= cur_rank:
                    count+=1
                sorted_rank_array[i] = (cur_id, count)

            """If all suffixes have different ranks then terminate the loop"""
            if sorted_flag:
                break

            self.map_to_rank_array(sorted_rank_array)
            k = k<<1

        """constrcust the suffix array using the rank array"""
        suffix_array = [None for i in range(len(self.rank_array))]
        for i in range(len(self.rank_array)):
            suffix_array[self.rank_array[i]] = i+1

        return suffix_array

# sa = SuffixArray()
# str1 = "MISSISSIPPI$"
# sa.build_suffix_array("JARARAKA$") #[9, 8, 6, 4, 2, 1, 7, 5, 3]

