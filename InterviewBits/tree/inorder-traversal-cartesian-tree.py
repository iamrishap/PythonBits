"""
Given an inorder traversal of a cartesian tree, construct the tree.
 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
 Note: You may assume that duplicates do not exist in the tree.
Example :
Input : [1 2 3]
Return :
          3
         /
        2
       /
      1
"""


# Note that the root is the max element in the whole array. Based on the info, can you figure out the position of the
# root in inorder traversal ? If so, can you separate out the elements which go in the left subtree and right subtree ?
# Once you have the inorder traversal for left subtree, you can recursively solve for left and right subtree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):

        root = TreeNode(A[0])
        i = 1
        while i < len(A):
            node = TreeNode(A[i])
            if A[i] > root.val:
                node.left = root
                root = node
            else:
                temp = root
                while (temp.right is not None) and temp.right.val > A[i]:
                    temp = temp.right
                if temp.right is None:
                    temp.right = node
                else:
                    x = temp.right
                    temp.right = node
                    node.left = x
            i += 1
        return root
