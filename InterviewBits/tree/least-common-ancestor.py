"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.
 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph
 (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
Example :
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
"""


# Linear solution using path calculation :
#
# 1) Find path from root to n1 and store it in a vector or array.
# 2) Find path from root to n2 and store it in another vector or array.
# 3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch
# Linear solution using recursion :
# We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent.
# The parent would then test its left and right subtree if each contain one of the two nodes. If yes, then the parent
# must be the LCA and we pass its parent up to the root. If not, we pass the lower node which contains either one of
# the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree
# does not contain either p or q) up.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer

    def findPath(self, root, path, k):
        if root is None:
            return False

        path.append(root.val)
        if root.val == k:
            return True
        if root.left is not None and self.findPath(root.left, path, k) or root.right is not None and self.findPath(
                root.right, path, k):
            return True
        path.pop()
        return False

    def lca(self, A, B, C):
        path1 = []
        path2 = []
        if not self.findPath(A, path1, B) or not self.findPath(A, path2, C):
            return -1
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break;
            i = i + 1
        return path1[i - 1]
