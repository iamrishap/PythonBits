"""
Given a binary tree, find its maximum depth.
The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2.
"""


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A == None:
            return 0
        else:
            return 1 + max(self.maxDepth(A.left),
                           self.maxDepth(A.right))
