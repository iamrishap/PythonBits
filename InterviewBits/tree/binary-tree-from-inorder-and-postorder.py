"""
Given inorder and postorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree.
Example :
Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]
Return :
            1
           / \
          2   3
"""


# Focus on the postorder traversal to begin with.
# The last element in the traversal will definitely be the root.
# Based on this information, can you identify the elements in the left subtree and right subtree ?
# ( Hint : Focus on inorder traversal and root information )
# Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and
# postorder traversal for the left and right subtree and you need to figure them out.
# Divide and conquer.
# Bonus points if you can do it without recursion.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not B:
            return None
        root_pos = A.index(B[-1])
        new_node = TreeNode(B[-1])
        new_node.left = self.buildTree(A[:root_pos], B[:root_pos])
        new_node.right = self.buildTree(A[root_pos + 1:], B[root_pos:-1])
        return new_node
