"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Skip the node where head->next != NULL && head->val == head->next->val.
# Make sure you take care of corner cases :
# 1) Do you handle repetitions at the end ? ex : 1 -> 1
# 2) Do you handle cases where there is just one element ? ex : 1
# 3) Do you handle cases where there is just one element repeated numerous times ? 1->1->1->1->1->1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        current = A
        next = current.next
        while current:
            while next and next.val == current.val:
                next = next.next
            current.next = next
            current = current.next
        return head
