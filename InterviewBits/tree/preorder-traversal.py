"""
Given a binary tree, return the preorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [1,2,3].
Using recursion is not allowed.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, node):
        stack = []
        stack.append(node)
        ans = []
        while len(stack) > 0:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right is not None:
                stack.append(temp.right)
            if temp.left is not None:
                stack.append(temp.left)
        return ans
