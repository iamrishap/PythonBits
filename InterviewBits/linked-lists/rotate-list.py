"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Since n may be a large number compared to the length of list. So we need to know the length of linked list.
# After that, move the list after the (l-n % l )th node to the front to finish the rotation.
# Ex: {1,2,3} k = 2 Move the list after the 1st node to the front
# Ex: {1,2,3} k = 5, In this case Move the list after (3-5 % 3=1)st node to the front.
# So the code has three parts.
# 1) Get the length
# 2) Move to the (l-n%l)th node
# 3) Do the rotation

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        temp = A
        lent = 0
        while temp.next is not None:
            lent += 1
            temp = temp.next
        lent += 1
        final = temp
        temp.next = A
        temp1 = A
        B = B % lent
        for i in range(B):
            temp1 = temp1.next
        temp2 = A
        while temp1 != final:
            temp1 = temp1.next
            temp2 = temp2.next
        ans = temp2.next
        temp2.next = None
        return ans
