"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
 of every node never differ by more than 1.
Example :
Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
"""


# For a BST, all values lower than the root go in the left part of root, and all values higher go in the
# right part of the root. For the tree to be balanced, we will need to make sure we distribute the elements almost
# equally in left and right part. So we choose the mid part of the array as root and divide the elements around it .
# Things to take care of :
# 1) Are you passing a copy of the array around or are you only passing around a reference ?
# 2) Are you dividing the array before passing onto the next function call or are you just specifying
# the start and end index ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A) == 0:
            return None
        mid = len(A) / 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root
