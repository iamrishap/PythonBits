"""
Given a linked list and a value x, partition it such that all nodes less than x come before
 nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Maintain 2 pointers - one which maintains all nodes less than x and another which
# maintains nodes greater than or equal to x.
# Keep going along our list. When we are at node that is greater than or equal to x,
# we remove this node from our list and move it to list of nodes greater than x.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head1 = ListNode(0)  # handle for nodes < B
        head2 = ListNode(0)  # handle for nodes >= B
        node1, node2 = head1, head2
        while A:
            if A.val < B:
                node1.next, node1, A = A, A, A.next
            else:
                node2.next, node2, A = A, A, A.next
        # Link the two lists
        node1.next = head2.next
        # Clear last pointer
        node2.next = None
        return head1.next
