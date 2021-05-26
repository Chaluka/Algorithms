"""

"""
__author__ = "Chaluka Salgado"


class Node:

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        self.parent = None

    def insert(self, value):
        if self.value == value:
            return False

        elif self.value < value:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
                return True
            else:
                return self.right.insert(value)

        else:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
                return True
            else:
                return self.left.insert(value)

    def find(self, value):
        if self.value == value:
            # print(self.parent.value)
            return self
        elif self.value < value and self.right is not None:
            return self.right.find(value)
        elif self.value > value and self.left is not None:
            return self.left.find(value)
        else:
            return False

    # def get_successor(self):
    #
    #     if self.value > value:
    #         if self.left is None:
    #             return self
    #         else:
    #             get_successor(self.left, value)
    #     elif self.value < value:
    #         if self.right is None:
    #             return self
    #         else:
    #             get_successor(self.right,value)

    def in_order(self):

        if self.left:
            self.left.in_order()
        print(self.value)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):

        if self.right:
            self.right.post_order()
        if self.left:
            self.left.post_order()
        print(self.value)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_to(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print_tree(self, traversal_order='in_order'):
        if traversal_order == 'in_order':
            self.root.in_order()
        elif traversal_order == 'pre_order':
            self.root.pre_order()
        elif traversal_order == 'post_order':
            self.root.post_order()
        else:
            return False
        return True

    def search(self, value):
        if self.root == None:
            return False
        else:
            return self.root.find(value)

    def remove(self, value):
        if self.root is not None:
            node = self.root.find(value)
            # node.in_order()
            if node is not None:
                # if node has no children, we can simply delete it
                if node.right is None and node.left is None:
                    if node.value > node.parent.value:
                        node.parent.right = None
                        return True
                    else:
                        node.parent.left = None
                        return True
                # if node has two children, either you can replace it with predecessor or successor.
                # here, we do replace with the successor
                elif node.right is not None and node.left is not None:
                    # you need to find the successor first and then swap values and delete. we know that always the
                    # successor is in right sub-tree and it would be the left most node
                    left_most = node.right
                    while left_most.left:
                        if left_most.left is not None:
                            left_most = left_most.left

                    link_to_node = 0  # indicates it's in left sub-tree
                    if left_most.value > left_most.parent.value:
                        link_to_node = 1  # indicates it's in right sub-tree

                    node.value = left_most.value

                    # node.in_order()
                    # now you need to delete the successor node accordingly
                    # since successor can't have a left child, we move right child up only if it there is one
                    # also, all the below nodes of the successor
                    if left_most.right is not None:
                        if link_to_node:
                            left_most.parent.right = left_most.right
                            return True
                        else:
                            left_most.parent.left = left_most.right
                            return True
                    else:
                        if link_to_node:
                            left_most.parent.right = None
                            return True
                        else:
                            left_most.parent.left = None
                            return True

                # if node has only one child
                else:
                    if node.right is not None:
                        child = node.right
                    else:
                        child = node.left

                    if node.value > node.parent.value:
                        node.parent.right = child
                        return True
                    else:
                        node.parent.left = child
                        return True



            else:
                return False
        else:
            return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert_to(12)
    bst.insert_to(86)
    bst.insert_to(5)
    bst.insert_to(34)
    bst.insert_to(51)
    bst.insert_to(8)
    bst.insert_to(1)

    # bst.print_tree('pre_order')
    x = bst.remove(12)

    bst.print_tree('in_order')
    bst.print_tree('post_order')
