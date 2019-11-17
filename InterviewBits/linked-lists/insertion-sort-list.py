"""
Sort a linked list using insertion sort.
We have explained Insertion Sort at Slide 7 of Arrays
Insertion Sort Wiki has some details on Insertion Sort as well.
Example :
Input : 1 -> 3 -> 2
Return 1 -> 2 -> 3
"""


# This is very much a simulation problem.
# The only trick is how do you move a node from ith position to jth position.
# How do you move the pointers to do so ? Would having a temporary node help ?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revert(node):
    """ Revert list in-place """
    prev = None
    while node:
        prev, node.next, node = node, prev, node.next
    return prev


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        """ This solution:
              * doesn't swap the values themselves
                  -> in Python it doesn't matter much,
                     but in general doing so would kind of defeat
                     one advantage of having a linked list
              * doesn't create new node
              * builds the output list in decreasing order
                  -> if input list is already sorted,
                     the complexity would be O(n)
        """
        source = A
        dest = None
        while source:
            prev = None
            node = dest
            # Find insertion point (between prev and node)
            while node and node.val > source.val:
                prev, node = node, node.next
            if prev is None:
                dest = source
            else:
                prev.next = source
            source.next, source = node, source.next
        return revert(dest)
