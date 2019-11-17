"""
Given a binary tree, flatten it to a linked list in-place.
Example :
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
"""


# If you notice carefully in the flattened tree, each node’s right child points to the next node of a
# pre-order traversal.
# Now, if a node does not have left node, then our problem reduces to solving it for the node->right.
# If it does, then the next element in the preorder traversal is the immediate left child. But if we make the
# immediate left child as the right child of the node, then the right subtree will be lost. So we figure out where
# the right subtree should go. In the preorder traversal, the right subtree comes right after the rightmost element
# in the left subtree.
# So we figure out the rightmost element in the left subtree, and attach the right subtree as its right child.
# We make the left child as the right child now and move on to the next node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, n):
        # stack for pre-order traversal
        s = [n]
        head = TreeNode(0)  # dummy
        res = head
        while len(s):
            # get last
            n = s.pop()
            if n:
                # add right
                s.append(n.right)
                # add left
                s.append(n.left)
                # add right node
                res.right = TreeNode(n.val)
                # update res
                res = res.right
        # remove dummy
        return head.right
