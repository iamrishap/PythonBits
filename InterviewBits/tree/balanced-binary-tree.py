"""
Given a binary tree, determine if it is height-balanced.
 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never
  differ by more than 1.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Example :
Input :
          1
         / \
        2   3
Return : True or 1
Input 2 :
         3
        /
       2
      /
     1
Return : False or 0
         Because for the root node, left subtree has depth 2 and right subtree has depth 0.
         Difference = 2 > 1.
"""


# A tree is balanced if :
# 1) Left subtree is balanced
# 2) Right subtree is balanced
# 3) And the difference is height of left and right subtree is atmost 1.
# Can you think of a way to simulate that with recursion ?
# Note that depth of a tree can also be calculated recursively as max(depth(rightSubtree), depth(leftSubtree)) + 1.

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None or A.left is None and A.right is None:
            return 1
        queue = [A]
        while len(queue) > 0:
            T = queue.pop()
            if T.left:
                queue.append(T.left)
                if not T.right and (T.left.left or T.left.right):
                    return 0
            if T.right:
                queue.append(T.right)
                if not T.left and (T.right.left or T.right.right):
                    return 0
        return 1
