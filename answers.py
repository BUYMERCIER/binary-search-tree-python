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

################################################################################
# Tests

C = BinTree(9, None, None)
D = BinTree(4, None, None)
B = BinTree(3, None, D)
A = BinTree(7, B, C)

print(bst_to_list(A))
