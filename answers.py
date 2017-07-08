__author__ = "K4LI"

################################################################################
# REQUIREMENTS

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
        l.append(T.key)
        if T.left != None:
            bst_to_list(B.left)
        if T.right != None:
            bst_to_list(B.right)
    return l

################################################################################
# Tests
