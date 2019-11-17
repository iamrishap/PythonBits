"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
For example, given following linked lists :
  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"""


# First thing to note is that all you would want to do is modify the next pointers. You don’t need to create new nodes.
# At every step, you choose the minumum of the current head X on the 2 lists, and modify your answer’s next
# pointer to X. You move the current pointer on the said list and the current answer.
# Corner case,
# Make sure that at the end of the loop, when one of the list goes empty,
# you do include remaining elemnts from the second list into your answer.
# Test case : 1->2->3 4->5->6

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, head1, head2):
        """ Merges two sorted linked lists.
        Time complexity: O(max(n, m)). Space complexity: O(1),
        n, m are lengths of the linked lists.
        """
        dummy = ListNode(None)
        curr = dummy
        while head1 and head2:  # choose node with min value from two lists
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:  # list1 is longer, add whatever is left from it
            curr.next = head1
        elif head2:
            curr.next = head2
        return dummy.next
