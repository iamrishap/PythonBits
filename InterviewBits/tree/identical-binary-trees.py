"""
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Example :
Input :
   1       1
  / \     / \
 2   3   2   3
Output :
  1 or True
"""


# When are the 2 trees the same ?
# When the root values are the same, and left subtree of both trees are same,
# and right subtree of both trees are the same.
# Can you think of very easy recursive solution based on the above fact ?


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        # will only come here if only one of them is None
        # would have returned from above condition otherwise
        elif A is None or B is None:
            return 0
        elif (A.val == B.val
              and self.isSameTree(A.left, B.left)
              and self.isSameTree(A.right, B.right)):
            return 1
        else:
            return 0
