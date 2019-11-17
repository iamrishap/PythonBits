"""
You are given two positive integers A and B. For all permutations of [1, 2, …, A], we create a BST.
Count how many of these have height B.
Notes:
Values of a permutation are sequentially inserted into the BST by general rules i.e in increasing order of indices.
Height of BST is maximum number of edges between root and a leaf.
Return answer modulo 109 + 7.
Expected time complexity is worst case O(N4).
1 ≤ N ≤ 50
For example,
A = 3, B = 1
Two permutations [2, 1, 3] and [2, 3, 1] generate a BST of height 1.
In both cases the BST formed is
    2
   / \
  1   3
Another example,
A = 3, B = 2
Return 4.
Next question, can you do the problem in O(N3)?
"""

# BST follows the property that all values in left subtree and less than value at current node and all values
# in right subtree are greater than current node.
# If we fix the root node, the BST formed will be unique.
# Also, the actual values that are being inserted in BST don’t matter. So, we can directly deal with number of values
# being inserted in BST instead of the actual values. This helps in defining states of DP.
# Now, what should be the states of DP? Of course, number of elements is one state. Other can be the height required.
# So, we define DP(N, M) as the number of permutations of N elements which when inserted into BSTs generate
# BSTs of height exactly M. Now, to define a recurrence, we’ll iterate over the root of BST we choose.
# We have N options and based on each option, the size of left and right subtrees are defined.
# If i’th element is choosen as root, the left subtree will now contain (i - 1)
# elements and right subtree will contain (N - i) elements.
# Now, at least one of these subtrees must have a height of (M - 1) because we are right now solving for height M.
# Again, we’ll iterate over the heights of left and right subtrees.
# Now, number of permutations to form left subtree of size x with some height are say, X.
# Also, we call these permutations set A.
# And similarly, number of permutations to form right subtree of size y with some height are say, Y.
# And we call these permutations set B.
# Now, we can choose any permutation from A and any permutation from B, to form a unique tree.
# So, there are total of X*Y permutations. Also, any sequence of size (x+y) can give the same BST if
# the mutual ordering of the permutation from set A and permutation of set B is maintained.
# There are choose(x + y, y) ways to do that. So, total ways are X*Y*choose(x + y, y).
# So, in terms of pseudo code:
# def rec(N, M):
#     if N<=1:
#         if M==0: return 1
#         return 0;
#     ret=0
#     for i=1 to N:
#         x = i-1
#         y = N-i
#         ret1=0
#         //iterate over height of left subtree
#         for j = 0 to M-2:
#             ret1 = ret1 + rec(x, j)*rec(y, M-1)
#         //iterate over height of right subtree
#         for j = 0 to M-2:
#             ret1 = ret1 + rec(y, j)*rec(x, M-1)
#         //add the case when both heights=M-1
#         ret1 = ret1 + rec(x, M-1)*rec(y, M-1)
#         ret = ret + ret1*choose(x+y, y)
#     return ret
# We can precalculate choose table in O(N*N).
# Also, take care of modulo arithmetic.

import math
from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def nCr(self, n, r):
        f = math.factorial
        return f(n) // (f(r) * f(n - r))

    def cntPermBST(self, n, height):
        return self.recurse(n, height)[0] % (10 ** 9 + 7)

    @memo
    def recurse(self, n, height):
        """
            Tuple: (# correct height, # less than correct height)
        """
        if n == 1 and height == 0:
            return [1, 0]
        elif n == 0 and height >= 0:
            return [0, 1]
        elif n == 0 or height == 0:
            return [0, 0]
        else:
            count = [0, 0]
            for i in range(1, n + 1):
                left = self.recurse(i - 1, height - 1)
                right = self.recurse(n - i, height - 1)
                num = left[0] * right[1] + right[0] * left[1] + left[0] * right[0]
                count[0] += self.nCr(n - 1, n - i) * num
                count[1] += self.nCr(n - 1, n - i) * left[1] * right[1]
            return count
