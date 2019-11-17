"""
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list,
 only nodes itself can be changed.
"""


# Lets first look at the problem of swapping 2 nodes.
# Method 1: Just swap the values in the 2 nodes. In most cases, this won’t be a permissible solution.
# Method 2: Move around the pointers.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = A.next if A and A.next else A
        while A and A.next:
            C = A.next.next  # 3rd Node
            D = C.next if C and C.next else C  # 4th Node if existing
            A.next.next, A.next, A = A, D, C
        return head
