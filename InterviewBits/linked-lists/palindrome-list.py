"""
Given a singly linked list, determine if its a palindrome.
Return 1 or 0 denoting if its a palindrome or not, respectively.
Notes:
Expected solution is linear in time and constant in space.
For example,
List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""


# To check palindrome, we just have to reverse latter half of linked list and then we can in (n/2)
# steps total can compare if all elements are same or not.
# For finding mid point, first we can in O(N) traverse whole list and calculate total number of elements.
# Reversing is again O(N).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        slow = A
        fast = A
        prev_of_slow = None
        while fast and fast.next:
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next.next

        if fast is None:
            prev_of_slow.next = None
        else:
            if prev_of_slow is not None:
                prev_of_slow.next = None
            mid = slow
            slow = slow.next

        # reverse the second half
        cur = slow
        prev = None
        while cur:
            fut = cur.next
            cur.next = prev
            prev = cur
            cur = fut

        first = A
        second = prev

        while first and second:
            if first.val != second.val:
                return 0
            first = first.next
            second = second.next

        return 1
