"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: Using library sort function is not allowed.
Example :
Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""


# There are multiple approaches possible here. We need to make sure we do not allocate extra memory.
# Approach 1:
#  Count the number of red, white and blue balls.
# Then in another pass, set initial redCount number of cells as 0, next whiteCount
# cell as 1 and next bluecount cells as 2.
# *Requires 2 pass of the array. *
# **Approach 2: **
#  Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array.
# 1s will automatically be in their right position.

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        B = [0, 0, 0]
        for i in A:
            B[i] += 1
        return [0] * B[0] + [1] * B[1] + [2] * B[2]
