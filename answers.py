__author__ = "K4LI"

################################################################################
# REQUIREMENTS

from toSVG.toSVG import *

class BinTree:
    def __init__(self, key, left, right):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right

################################################################################
# Exercises

# 1.1 Write a function that builds a sorted list with the elements of a binary
# search tree.

def bst_to_list(T, l = []):
    if T == None:
        return None
    else:
        if T.left != None:
            bst_to_list(T.left, l)
        l.append(T.key)
        if T.right != None:
            (bst_to_list(T.right, l))
    return l

# 1.2 Write a function that builds a balanced binary search tree using a sorted
# list.

def list_to_avl(l, B = BinTree(None, None, None)):
    if len(l) == 0:
        return None
    else:
        B.key = l[len(l) // 2]
        l.pop(len(l) // 2)
        if len(l) > 0:
            B.left = list_to_avl(l[:(len(l) // 2):])
            B.right = list_to_avl(l[(len(l) // 2)::])
        return B

################################################################################
# Tests

C = BinTree(9, None, None)
D = BinTree(4, None, None)
B = BinTree(3, None, D)
A = BinTree(7, B, C)

l = bst_to_list(A)
print(l)
tree = list_to_avl(l)
toSVG(tree, "bst")
