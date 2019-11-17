"""
Given a binary tree, invert the binary tree and return it.
Look at the example for more details.
Example :
Given binary tree
     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return
     1
   /   \
  3     2
 / \   / \
7   6 5   4
"""


# Think recursively.
# On every node, you need to invert the left and right subtree and then swap them.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if not A:
            return None
        ileft = self.invertTree(A.left)
        iright = self.invertTree(A.right)
        A.left, A.right = iright, ileft
        return A
