"""
This implementation contains the burrows wheeler algorithm
"""

__author__ = "Chaluka Salgado"
__copyright__ = "Copyright 2020, FIT2004 Teaching Materials"
__email__ = "chaluka.salgado@gmail.com"
__docformat__ = 'reStructuredText'

from typing import TypeVar, List
from copy import deepcopy
from suffix_array import SuffixArray

T = TypeVar('T')


class BurrowsWheelerCompressor:
    DOMAIN_SIZE = 27

    def __init__(self)->None:
        self.string = None
        self.rank_array = [None]*self.DOMAIN_SIZE

    def compress(self, string:str)->str:
        """ We use suffix array to compress the given string"""
        sa = SuffixArray()
        sufiix_array = sa.build_suffix_array(string)

        bwt = []
        for i in range(len(sufiix_array)):
            # if we have the suffix array, using Last-First property,
            # we can easily construct the bwt by referring to the previous character
            index = sufiix_array[i]-2 #rank starting from 1 so need -2
            bwt.append(string[index])

        return  "".join(bwt)

    def __initiate_lf_mapping(self, bwt:str):

        n = len(bwt)
        rank = dict()
        count = dict()
        occ = [0 for i in range(n)]
        # fill count array
        counter = 0
        for char in bwt:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
                rank[char] = 1
            occ[counter] = count[char] - 1
            counter += 1

        for i in range(1, len(count)):
            prev = sorted(count)[i - 1]
            cur = sorted(count)[i]
            rank[cur] = rank[prev] + count[prev]

        return rank, occ

    def decompress(self,bwt:str)->str:


        rank, occ = self.__initiate_lf_mapping(bwt)
        out_str = ['$']
        index = 0
        while bwt[index] != '$':
            out_str = [bwt[index]] + out_str
            index = occ[index] + rank[bwt[index]]-1


        return "".join(out_str)



    def substring_search(self,sub_str:str, bwt:str)->bool:

        rank, occ = self.__initiate_lf_mapping(bwt)
        n = len(bwt)
        found = False
        scope = [0,n-1]
        counter = len(sub_str)-1

        while (scope[1] - scope[0]) >0 or not found:
            char = sub_str[counter]
            temp = []
            # print("------")
            for i in range(scope[0],scope[1]+1):
                # print(bwt[i])
                if bwt[i] == char:
                    temp.append(occ[i] + rank[bwt[i]] - 1)

            if counter == 0 and len(temp)!=0:
                found = True
                break

            if len(temp)==0:
                break
            scope = [temp[0],temp[-1]]
            counter-=1

        return found



if __name__ == "__main__":
    # bwt = "IPSSM$PISSII"
    b = BurrowsWheelerCompressor()

    # bwt = b.compress("MISSISSIPPI$")
    # c = b.decompress(bwt)
    # print(c)
    x = b.substring_search('wol','oooloooolwml$')
    print(x)





