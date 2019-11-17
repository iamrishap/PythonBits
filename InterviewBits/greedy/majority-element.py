"""
Given an array of size n, find the majority element.
 The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example :
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""


# If we cancel out each occurrence of an element e with all the other elements that are different from e then e will
# exist till end if it is a majority element. Loop through each element and maintains a count of the element that has
# the potential of being the majority element. If next element is same then increments the count, otherwise decrements
# the count. If the count reaches 0 then update the potential index to the current element and reset count to 1.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        curr_majority = A[0]
        cnt = 1
        for x in A[1:]:
            if x != curr_majority:
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                curr_majority = x
                cnt = 1

        return curr_majority
