"""
Given a binary tree T, find the maximum path sum.
The path may start and end at any node in the tree.
Input Format:
The first and the only argument contains a pointer to the root of T, A.
Output Format:
Return an integer representing the maximum sum path.
Constraints:
1 <= Number of Nodes <= 7e4
-1000 <= Value of Node in T <= 1000
Example :
Input 1:
       1
      / \
     2   3
Output 1:
     6
Explanation 1:
    The path with maximum sum is: 2 -> 1 -> 3
Input 2:
       -10
       /  \
     -20  -30
Output 2:
    -10
Explanation 2
    The path with maximum sum is: -10
"""


# There are several ways of looking at this problem.
# If we knew that root R is going to be a part of the longest path. Then we can look at the longest path to any
# leaf in the left subtree, longest path in the right subtree, and add them up along with root’s value to get the
# answer ( Obviously we only consider a path if its value is not negative ). To calculate the longest path till a leaf
# is O(n) [ Recursive call carrying forward the cumulative sum to a node ].
# Given N possible roots, and then the O(n) leaf path calculation, the bruteforce becomes O(n^2).
# However, note that the calculation of the longest path to the leaf is very redundant. So, to calculate the
# result for root R, can you reuse the results you have for R->left / R->right ?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        res = [-2 ** 31]

        def maxPathSumUtil(root):
            if root is None:
                return 0
            l = maxPathSumUtil(root.left)
            r = maxPathSumUtil(root.right)
            max_single = max(max(l, r) + root.val, root.val)
            max_top = max(max_single, l + r + root.val)
            res[0] = max(res[0], max_top)
            return max_single

        maxPathSumUtil(root)
        return res[0]
