"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given sum.
Example :
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# Recursion might make this problem much easier to solve.
# You just need to keep a track of the sum from the root to the current node.
# Then it becomes a question of just checking if the current node is a leaf node, and if so, do the sum match.

# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0
        else:
            if A.val == B and not A.left and not A.right:
                return 1
            else:
                if self.hasPathSum(A.left, B - A.val):
                    return 1
                if self.hasPathSum(A.right, B - A.val):
                    return 1
        return 0
