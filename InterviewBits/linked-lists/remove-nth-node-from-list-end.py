"""
Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
"""


# Obviously, since we do not have back pointers, reaching the end node and then making our way back is not an option.
# There are 2 approaches :
# 1) Find out the length of the list in one go. Then you know the number of node to be removed.
# Traverse to the node and remove it.
# 2) Make the first pointer go n nodes. Then move the second and first pointer simultaneously.
# This way, the first pointer is always ahead of the second pointer by n nodes. So when first pointer
# reaches the end, you are on the node to be removed.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count = count + 1

        if fast is None:
            temp = head
            if head is not None:
                head = head.next
            temp = None
            return head
        prev_of_slow = None
        while slow and fast:
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next

        prev_of_slow.next = slow.next
        slow = None
        return head
