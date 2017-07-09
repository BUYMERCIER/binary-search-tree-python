__author__ = "K4LI"

################################################################################
# REQUIREMENTS

from toSVG.toSVG import *
from os import *

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

# 1.1.1 Write a function that builds a sorted list with the elements of a binary
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

# 1.1.2 Write a function that builds a balanced binary search tree using a
# sorted list.

def listToAVL (L, l, r):
	if l < r:
		m = (l+r)//2
		T = BinTree(L[m], None, None)
		T.left = listToAVL(L, l, m)
		T.right = listToAVL(L, m+1,r)
		return T

# 1.2 Write a function that tests whether a binary tree is a search tree or not.

def isBST(T):
    pass

# 2.1 (Researches)
# 2.1.1 (a) Where are the maximum and the minimum values in a non-empty binary
# search tree?

"""
The maximum value of a BST is stored in the most right leaf.
The minimum value of a BST is stored in the most left leaf.
"""

# 2.1.1 (b) Write the two functions minBST(B) and maxBST(B), where B is a non
# empty BST.

def minBST(B):
    if B != None:
        if B.left == None:
            return B.key
        else:
            return minBST(B.left)

def maxBST(B):
    if B != None:
        if B.right == None:
            return B.key
        else:
            return maxBST(B.right)

# 2.1.2 Write a function that searches a value x in a binary search tree. It
# returns the tree whose root contains x if found, the value None otherwise.

def searchBST(B, x):
    if B == None:
        return None
    else:
        if B.key == x:
            return B
        elif x < B.key:
            return searchBST(B.left, x)
        else:
            return searchBST(B.right, x)

# 2.2.1 Use the insertion at the leaf principle to create the binary search tree
# obtained, from an empty tree, by successive insertions of the following values
# (in that order):
# 13,20,5,1,15,10,18,25,4,21,27,7,12

# 2. Write a function that adds an element to a binary search tree.

def insertBST(B, x):
    if B == None:
        return BinTree(x, None, None)
    else:
        if x == B.key:
            return False
        elif x < B.key:
            B.left = insertBST(B.left, x)
        elif x > B.key:
            B.right = insertBST(B.right, x)
        return B

################################################################################
# Tests

C = BinTree(9, None, None)
D = BinTree(4, None, None)
B = BinTree(3, None, D)
A = BinTree(7, B, C)

tree = listToAVL([1,2,3,4,5,6,8,7,9], 0, 9)
tree = insertBST(tree, 10)
toSVG(tree, "bst")
print(minBST(tree))
print(maxBST(tree))
