"""
Remove Element
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.
 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
"""

# Maybe you should try maintaining 2 pointers in the array:
# One pointer iterates over the array
# Other pointer only moves when it finds an element different from ‘elem’.
# In other words, the second pointer only moves when the first pointer is on an element
# worth keeping in the final array.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        """ Maintain position of free slot.
            We shift any valid element in this slot.
        """
        slot = 0
        for x in A:
            if x != B:
                # May replace an element by itself, nevermind.
                A[slot] = x
                slot += 1
        return slot
