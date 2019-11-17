"""
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 Note:
You may only use constant extra space.
Example :
Given the following binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
 Note 1: that using recursion has memory overhead and does not qualify for constant space.
Note 2: The tree need not be a perfect binary tree.
"""


# Lets say you have already created next pointers till level L. To create next
# pointer for level L+1, start with the first node on level L.
#         1   ->  2   ->  3  -> 4
#        /         \           / \
#       /           \         /    \
#      5            6        7      8
#
#
#         1   ->  2   ->  3  -> 4
#        /         \           / \
#       /           \         /   \
#      4     ->      7   ->  8 ->  9
# Keep track of the previous node you encountered on the next level. For the current node, explore the left and
# right child if they are not null in that order. If the prev is not set, that means we are looking at the leftmost
# node on the next level ( Lets store it because we will begin the next iteration from this node ). Else you can
# assign prev->next as the current node in next level you are exploring and update the prev node.

class Solution:

    def populate_next_r_02(self, root):
        if root is None:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                head = root
                while head.next:
                    if head.next.left:
                        root.left.next = head.next.left
                        break
                    elif head.next.right:
                        root.left.next = head.next.right
                        break
                    head = head.next
        if root.right:
            head = root

            while head.next:
                if head.next.left:
                    root.right.next = head.next.left
                    break
                elif head.next.right:
                    root.right.next = head.next.right

                head = head.next
        self.populate_next_r_02(root.right)
        self.populate_next_r_02(root.left)
