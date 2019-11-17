"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Skip the node where head->next != NULL && head->val == head->next->val. Maintain a “pre”
# ode which is the node just previous to the block of head you are checking.
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
        curr = A
        head = prev = ListNode(None)
        head.next = curr
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # still one one of duplicate values left so advance
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return head.next
