"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
"""


# Recursion might make this problem much easier to solve.
# You just need to keep a track of :
# 1) the sum from the root to the current node.
# 2) The elements encountered from the root to this node.


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        self.paths = []

        def path_sum_rec(root, sum_, curr_path):
            if root.left is None and root.right is None:
                if sum_ - root.val == 0:
                    self.paths.append(curr_path + [root.val])
                return
            if root.left is not None:
                path_sum_rec(root.left, sum_ - root.val, curr_path + [root.val])
            if root.right is not None:
                path_sum_rec(root.right, sum_ - root.val, curr_path + [root.val])

        if A is not None:
            path_sum_rec(A, B, [])

        return self.paths
