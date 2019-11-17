"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
Example :
    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# 2 trees T1 and T2 are symmetric if
# 1) value of T1’s root is same as T2’s root
# 2) T1’s left and T2’s right are symmetric.
# 3) T2’s left and T1’s right are symmetric.
# Can you use the above fact to model an easy recursion based solution ?


class Solution:

    def _isSymmetric(self, a, b):
        if a is None:
            return b is None
        if b is None:
            return a is None
        return a.val == b.val and \
               self._isSymmetric(a.right, b.left) and \
               self._isSymmetric(a.left, b.right)

    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return 1 if self._isSymmetric(A.left, A.right) else 0
