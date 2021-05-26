"""
This is the FIT2085 implementation of Binary Tree

"""
from linked_list import LinkedList
from typing import TypeVar, Generic, Callable, List
K = TypeVar('K')
I = TypeVar('I')

class BinarySearchTreeNode(Generic[K, I]):

    def __init__(self, key: K, item:I=None)->None:
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def __str__(self)->str:
        return "( " + str(self.key) + " , " + str(self.item) + " )"


class BinarySearchTree(Generic[K, I]):

    def __init__(self)->None:
        self.root = None

    def is_empty(self)->bool:
        return self.root is None

    def __len__(self):
        return self._len_aux(self.root)

    def _len_aux(self, current:BinarySearchTreeNode[K, I])->int:
        if current is None:
            return 0
        else:
            return 1+ self._len_aux(current.left) + self._len_aux(current.left)


    # def find(self, key:K)->bool:
    #     return self.find_aux(self.root, key)

    def find_aux(self, current: BinarySearchTreeNode[K, I], key, K)->bool:
        if current is None:
            return False
        elif current.key == key:
            return True
        elif key < current.key:
            return self.find_aux(current.left, key)
        else:
            return self.find_aux(current.right, key)

    def __contains__(self, key:K):
        return self.find_aux(self.root, key)

    def __getitem__(self, key: K) -> I:
        return self.getitem_aux(self.root, key)

    def getitem_aux(self, current: BinarySearchTreeNode[K, I], key: K) -> I:
        if current is None:  # base case: empty
            raise KeyError("Key not found")
        elif key == current.key:  # base case: found
            return current.item
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            return self.getitem_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BinarySearchTreeNode[K, I], key: K, item: I) -> None:
        if current is None:  # base case: at the leaf
            current = BinarySearchTreeNode(key, item)
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            current.item = item
        return current

    def height(self):
        return self.height_aux(self.root)

    def height_aux(self, current: BinarySearchTreeNode[K,I]):
        if current is None:
            return 0
        else:
            return 1 + max(self.height_aux(current.left), self.height_aux(current.right))

    def is_leaf(self, node: BinarySearchTreeNode[K,I])->bool:
        return node.left is None and node.right is None

    def get_leaves(self) -> LinkedList:
        a_list = LinkedList(len(self))
        self.get_leaves_aux(self.root, a_list)
        return a_list

    def get_leaves_aux(self, current: BinarySearchTreeNode[K, I], a_list: LinkedList) -> None:
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, a_list)
                self.get_leaves_aux(current.right, a_list)

    def sum_leaves(self)->int:
        return self.sum_leaves_aux(self.root)

    def sum_leaves_aux(self, current:BinarySearchTreeNode[K,I])->int:
        if current is None:
            return 0
        elif self.is_leaf(current):
            return current.item
        else:
            return self.sum_leaves_aux(current.left) + self.sum_leaves_aux(current.right)

    def in_between(self, a: K, b:K)->List[I]:
        lst=[]
        self.in_between_aux(self.root, a,b,lst)
        return lst

    def in_between_aux(self, current: BinarySearchTreeNode[K,I], a: K, b:K, lst:List[I])->None:
        if current is not None:
            if current.key > a:
                self.in_between_aux(current.left,a,b,lst)
            # if current.key > a and current.key < b:
            if a <=  current.key <= b:
                lst.append(current.item)
            if current.key < b:
                self.in_between_aux(current.right,a,b,lst)

    def pre_order(self, f:Callable)->None:
        self.pre_order_aux(self.root, f)

    def pre_order_aux(self, current: BinarySearchTreeNode[K, I], f:Callable)->None:
        if current is not None:
            f(current.item)
            self.pre_order_aux(current.left)
            self.pre_order_aux(current.right)


    def k_largest(self,k:int)->I:
        lst = []
        self.k_largest_aux(self.root, k, lst)
        return lst[-1]

    def k_largest_aux(self, current: BinarySearchTreeNode[K,I],k,lst)->None:
        if current is not None:
            print(current.item)
            self.k_largest_aux(current.right,k,lst)
            if len(lst) < k:
                lst.append(current.item)
                self.k_largest_aux(current.left,k,lst)


    def find_min(self)->K:
        if self.root is None:
            return None
        else:
            return self.find_min_aux(self.root)

    def find_min_aux(self, current:BinarySearchTreeNode[K,I])->K:
        if current.left is None:
            return current.key
        else:
            self.find_min_aux(current.left)

if __name__=="__main__":
    b = BinarySearchTree()
    b[5] = 5
    b[1] = 1
    b[9] = 9
    b[8] = 8
    b[3] = 3
    b[4] = 4
    b[2] = 2
    b[10] = 10
    b[7] = 7
    b[6] = 6
    print("---", b.k_largest(3))