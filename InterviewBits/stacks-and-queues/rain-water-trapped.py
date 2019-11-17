"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
Input Format
The only argument given is integer array A.
Output Format
Return the total water it is able to trap after raining..
For Example
Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
Explaination 1: <img src="http://i.imgur.com/0qkUFco.png">
    In this case, 6 units of rain water (blue section) are being trapped.
"""


# instead of calculating area by height*width, we can think it in a cumulative way. In other words,
# sum water amount of each bin(width=1). Search from left to right and maintain a max height of left
# and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water
# from the lower part. For example, if current height of left is lower, we fill water in the left bin.
# Until left meets right, we filled the whole container.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        # Visits each element of the array A twice
        # (stacking and popping).
        # If the stack is implemented in a more basic
        # form and stack[0] is not a fast operation,
        # we could store the current maximal element
        # separately.
        stack = []
        water = 0
        for a in A:
            if stack and stack[0] <= a:
                h = stack[0]
                while stack:
                    water += h - stack.pop()
            stack.append(a)
        h = stack.pop()
        while stack:
            n = stack.pop()
            if n > h:
                h = n
                continue
            water += h - n
        return water


A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

s = Solution()
print(s.trap(A))
