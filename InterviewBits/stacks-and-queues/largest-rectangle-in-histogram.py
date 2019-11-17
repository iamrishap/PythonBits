"""
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.
Largest Rectangle in Histogram: Example 1
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
Largest Rectangle in Histogram: Example 2
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Find the area of largest rectangle in the histogram.
Input Format
The only argument given is the integer array A.
Output Format
Return the area of largest rectangle in the histogram.
For Example
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""


# Whats the brute force approach here?
#
# We know that the height of the largest rectange will be one of the heights of the histogram (Think about why?)
# If that is the case, we can iterate on all the histograms, and for each histogram H, we try to create the maximum
# rectange with H as the height.
# To do that, we keep going left L and right R till we encounter a histogram with height less than H.
# Now, (R - L - 1) * H is one of the possibilities for the largest rectangle.
# Doing this for all the histograms will give us the right solution.
# Following is a rough pseudocode for the approach mentioned above :
# max_rectangle = 0
# for index = 0 to all_histograms.length
#   H = all_histograms[index]
#   L = index, R = index
#   while L >= 0 AND all_histograms[L] >= H
#     L = L - 1
#   while R < all_histograms.length AND all_histograms[R] >= H
#     R = R + 1
#   max_rectangle = MAX(max_rectangle, (R - L - 1) * H)
# return max_rectangle
# This approach is however O(N^2) time complexity in the worst case. How can we do better than this approach?
# Hint : Think in terms of using a stack ?
# As discussed in the previous hint, height of the maximum rectangle will be height of one of the histograms.
# For each histogram H, we need to know index of the first smaller (smaller than H) bar on left of H (lets call it L)
# and index of first smaller bar on right of H.
# We already tried the brute force approach. How can we do better?
# Important observation:
# Lets consider 2 consecutive histograms H[i] and H[i+1]. Lets assume H[i+1] < H[i]
# In such a case, for all histograms X with index > i + 1 when traversing left for L, there is no point looking
# at H[i] after looking at H[i+1]. If H[i+1] > X, obviously H[i] > X as we already know H[i] > H[i+1]
# Then, whats the next entry we would want to look at? We would want to look at the first histogram
# left of H[i+1] with height less than H[i+1].
# Can you think of a stack based approach based on the above observation?

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        result = 0

        i = 0
        while i < len(A):
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
                if result < tmp:
                    result = tmp

        while stack:
            tp = stack.pop()
            tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
            if result < tmp:
                result = tmp

        return result
