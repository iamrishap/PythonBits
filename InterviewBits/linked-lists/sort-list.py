"""
Sort a linked list in O(n log n) time using constant space complexity.
Example :
Input : 1 -> 5 -> 4 -> 3
Returned list : 1 -> 3 -> 4 -> 5
"""


# Can implement either merge sort or qsort.
# Lets look at merge sort. Traverse the linked list to find the mid point of the list. Now sort the first half and
# second half separatly by calling the function on them. Then merge the 2 lists ( Note that we already
# have solved a problem to merge 2 lists ).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(A, B):
    i = A;
    j = B
    # i is the pointer to the current node in A
    # j is the pointer to the current node in B
    first = None;
    last = None
    # first is the first node in the sorted list
    # last is the last node in the sorted list
    while i and j:
        # choose node with the minimum value, and update the current one
        if i.val < j.val:
            min_n = i;
            i = i.next
        else:
            min_n = j;
            j = j.next
        # update last and first
        if last is None:
            first = last = min_n
        else:
            last.next = min_n;
            last = min_n
    # extend the rest to the list
    while i:
        last.next = i;
        last = i;
        i = i.next
    while j:
        last.next = j;
        last = j;
        j = j.next
    last.next = None
    return first


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None:
            return A
        i = A;
        n = 0
        while i is not None:
            i = i.next;
            n += 1
        # now n = len(A)
        mid = A
        for t in range(n // 2 - 1):
            mid = mid.next
        B = mid.next
        mid.next = None
        return mergeTwoLists(self.sortList(A), self.sortList(B))
