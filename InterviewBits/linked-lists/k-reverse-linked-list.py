"""
Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
 NOTE : The length of the list is divisible by K
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
Try to solve the problem using constant extra space.
"""


# Split the list into buckets of length K and then reverse each of them. After this you have to concatenate the buckets
# and return the list. To split the list into buckets of length K, use 2 pointers that are K elements afar.
# To reverse a linked list check this.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        cur = start = A  # cur tracks the current node, start marks the beg. of bucket
        n = 1  # counter to track current bucket size
        while cur:
            if n < B:
                n += 1
                next = cur.next
                if next:
                    cur.next = next.next
                    if start == A:
                        next.next = start
                        A = next
                        start = A
                    else:
                        next.next = start.next
                        start.next = next
            else:  # bucket full, reset the variables
                start = cur
                cur = cur.next
                n = 1
        return A
