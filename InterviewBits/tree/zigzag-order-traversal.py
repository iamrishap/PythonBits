"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right,
then right to left for the next level and alternate between).
Example :
Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return
[
         [3],
         [20, 9],
         [15, 7]
]
"""


# We will be using 2 stacks to solve this problem. One for the current layer and other one for the next layer.
# Also keep a flag which indicates the direction of traversal on any level.
# You need to pop out the elements from current layer stack and depending upon the value of flag push the
# childs of current element in next layer stack. You should maintain the output sequence in the process as well.
# Remember to swap the stacks before next iteration. When should you terminate this algorithm?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if A is None:
            return []
        lr, rl = [], [A]
        st = rl
        lr_status = True
        result = []
        while st:
            level = []
            for _ in range(len(st)):
                x = st.pop()
                level.append(x.val)
                if lr_status:
                    if x.left:
                        lr.append(x.left)
                    if x.right:
                        lr.append(x.right)
                else:
                    if x.right:
                        rl.append(x.right)
                    if x.left:
                        rl.append(x.left)
            if lr_status:
                st = lr
            else:
                st = rl
            lr_status = not lr_status
            result.append(level)
        return result
