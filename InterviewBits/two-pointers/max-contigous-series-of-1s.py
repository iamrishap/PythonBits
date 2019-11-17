"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.
For this problem, return the indices of maximum continuous series of 1s in order.
Example:
Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1
Output :
[0, 1, 2, 3, 4]
If there are multiple possible solutions, return the sequence which has the minimum start index.
"""


# Lets take an example:
# N : 4
# lis : 1 0 1 0
# M : 2
# pointer i and j
# i = j = 0
# iterate till i < N:
#         if(Number_of_Zeros_in_Current_range > M) :
#                 increment j and reduce range till Number_of_Zeros_in_current_range < M
#         else :
#                 add element in range and update all variables


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, array, m):
        """ Returns indices of longest sequence of consecutive 1s that can be
        achieved by flipping m 0s.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        i, j = 0, 0  # start, end of current consecutive 1s sequence
        x, y = 0, 0  # start, end of longest consecutive 1s sequence
        while j < n:
            if array[j]:  # current element is 1
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                j += 1  # move the right pointer
            elif not array[j] and m > 0:  # current element is 0, we can flip it
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                m -= 1  # deacrese number of allowed flips
                j += 1  # move the right pointer
            else:  # current element is zero and we are out of flips
                if not array[i]:  # start of current 1s sequence is 0
                    m += 1  # increase available flips
                i += 1  # move the left pointer
        return list(range(x, y + 1))
