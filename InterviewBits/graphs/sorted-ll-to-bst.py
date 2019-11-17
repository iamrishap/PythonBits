"""
Given a singly linked list where elements
are sorted in ascending order, convert it to a height balanced BST.
A height balanced BST : a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
Example :
Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3

"""
import os
os.path.abspath(__file__ + "/../../")
from DataStructure.treeNode import Node as TreeNode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if not A:
            return
        if not A.next:
            return TreeNode(A.val)

        slow, fast = A, A.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(A)
        root.right = self.sortedListToBST(tmp.next)

        return root


_ = ListNode(7)
__ = ListNode(6)
__.next = _
_ = ListNode(5)
_.next = __
__ = ListNode(4)
__.next = _
_ = ListNode(3)
_.next = __
__ = ListNode(2)
__.next = _
A = ListNode(1)
A.next = __
s = Solution()
s.sortedListToBST(A).display()
