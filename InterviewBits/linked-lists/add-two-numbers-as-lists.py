"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
"""


# Very much the simulation of the mathematical process of summing up the numbers.
# You sum the digits and maintain a carry.
# Gotchas :
# 1) What if one list if shorter than the other ? 1->2 + 2->3->4->5
# 2) What if the answer has more digits ? 1 + 9

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ptr1 = A
        ptr2 = B
        carry = 0
        while ptr1 and ptr2:
            sumi = carry + ptr1.val + ptr2.val
            ptr2.val = sumi % 10
            carry = sumi // 10
            prev = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr1:
            prev.next = ptr1
            while ptr1:
                sumi = carry + ptr1.val
                ptr1.val = sumi % 10
                carry = sumi // 10
                prev = ptr1
                ptr1 = ptr1.next
        while ptr2:
            sumi = carry + ptr2.val
            ptr2.val = sumi % 10
            carry = sumi // 10
            prev = ptr2
            ptr2 = ptr2.next
        if carry != 0:
            prev.next = ListNode(carry)
        return B
