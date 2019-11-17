"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers % 1003.
Example :
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""


# Think recursion.
# Carrying along the number formed from root to the node when calling the function for node, will make stuff easier for
# you. When you encounter a new digit, you can append it to existing one as newNum = oldNum * 10 + newDigit.

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.sum1 = 0;

    def helper(self, A, sum1, string=""):
        if A is None:
            return

        if A.left is None and A.right is None:
            string += str(A.val)
            self.sum1 = (self.sum1 % 1003 + int(string) % 1003) % 1003
            return

        string += str(A.val)
        self.helper(A.left, sum1, string)
        self.helper(A.right, sum1, string)

    def sumNumbers(self, A):
        if A is None:
            return 0;

        sum1 = 0
        self.helper(A, sum1)
        return self.sum1
