"""
Given a binary tree, return the inorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [1,3,2].
Using recursion is not allowed
"""


# Instead of calling the functions, can you put the nodes on a stack and process them ?
# How would your solution work if you were allowed to change the original tree ?
# How would it work if you were not allowed to change the tree but use additional memory
# ( track the number of times a node has appeared in the tree ) ?
# How would it work if you were not even allowed the extra memory ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        curnode = A
        values = []
        stack = []
        while True:
            if curnode is not None:
                stack.append(curnode)
                curnode = curnode.left
            else:
                if len(stack) > 0:
                    curnode = stack.pop()
                    values.append(curnode.val)
                    curnode = curnode.right
                else:
                    return values
