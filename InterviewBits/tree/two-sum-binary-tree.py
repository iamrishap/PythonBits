"""
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether
or not there exist two different nodes A and B such that A.value + B.value = K.
Return 1 to denote that two such nodes exist. Return 0, otherwise.
Notes
Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :
Input 1:
T :       10
         / \
        9   20
K = 19
Return: 1
Input 2:
T:        10
         / \
        9   20
K = 40
Return: 0
"""


# How would you solve with O(N) memory? Let’s say you are given a sorted array and you need to find two indices i < j,
# such that A[i] = A[j]. Can you relate between a sorted array and a BST? Can you avoid O(N) memory
# and do with O(height) memory?
# If you do inorder traversal of BST you visit elements in increasing order. So, we use a two pointer approach,
# where we keep two pointers pt1 and pt2. Initially pt1 is at smallest value and pt2 at largest value.
# Then we compare sum = pt1.value + pt2.value. If sum < target, we increase pt2,
# else we decrease pt2 until we reach target.
# Using the same concept used in
# https://www.interviewbit.com/courses/programming/topics/trees/problems/treeiterator/ we can do this.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, k):
        if self.helper(root, k, {}) is True:
            return 1
        else:
            return 0

    def helper(self, root, k, store):

        if root is None:
            return False
        subtractedValue = k - root.val
        if subtractedValue not in store:
            store[root.val] = subtractedValue
        else:
            return True
        return self.helper(root.left, k, store) or self.helper(root.right, k, store)
