"""
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal 
of the tree when the depth of the tree is much greater than number of nodes on a level.
"""""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "val: {}, left: ({}), right: ({})".format(self.val, self.left, self.right)


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        from collections import deque
        q = deque()
        result = []
        level = []
        if A:
            q.append(A)
            q.append(None)  # Marker signifying end of a level
        else:
            return []
        while len(q) > 0:
            item = q.popleft()
            if item:
                level.append(item.val)  # Creating a list of items in this level
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                result.append(level)
                # Add None marker, only when there are items left to process, otherwise it will be infinite loop
                if len(q) > 0:
                    level = []
                    q.append(None)
        return result


root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(20)
rl = TreeNode(15)
rr = TreeNode(7)
r.left = rl
r.right = rr
root.right = r
root.left = l
print(root)
s = Solution()
print(s.levelOrder(root))
