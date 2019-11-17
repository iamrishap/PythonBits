"""
Given a binary tree, return the postorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [3,2,1].
Using recursion is not allowed.
"""


# Instead of calling the functions, can you put the nodes on a stack and process them ?
# Would the solution be easier if you were to print the reverse of the asked ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        result = [];
        d = [A]
        while d:
            node = d.pop()
            if node:
                result.append(node.val)
                d.append(node.left)
                d.append(node.right)
        return result[::-1]
