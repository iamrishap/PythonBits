"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example:
Given [5, 7, 7, 8, 8, 10]
and target value 8,
return [3, 4].
"""


# First, let us find the left boundary of the range.
# We initialize the range to [i=0, j=n-1]. In each step, calculate the middle element [mid = (i+j)/2].
# Now according to the relative value of A[mid] to target, there are three possibilities:
# If A[mid] < target, then the range must begin on the right of mid (hence i = mid+1 for the next iteration)
# If A[mid] > target, it means the range must begin on the left of mid (j = mid-1)
# If A[mid] = target, then the range must begins on the left of or at mid (j= mid)
# Since we would move the search range to the same side for case 2) and 3), we might as well merge
# them as one single case so that less code is needed:
# 2*. If A[mid] >= target, j = mid;
# Surprisingly, 1 and 2* are the only logic you need to put in loop while (i < j). When the while loop terminates,
# the value of i/j is where the start of the range is. Why?
# No matter what the sequence originally is, as we narrow down the search range, eventually we will be at a situation
# where there are only two elements in the search range.
# Suppose our target is 5, then we have only 7 possible cases:
# Case 1: [5 7] (A[i] = target < A[j])
# Case 2: [5 3] (A[i] = target > A[j])
# Case 3: [5 5] (A[i] = target = A[j])
# Case 4: [3 5] (A[j] = target > A[i])
# Case 5: [3 7] (A[i] < target < A[j])
# Case 6: [3 4] (A[i] < A[j] < target)
# Case 7: [6 7] (target < A[i] < A[j])
# For case 1, 2 and 3, if we follow the above rule, since mid = i => A[mid] = target
# in these cases, then we would set j = mid.
# Now the loop terminates and i and j both point to the first 5.
# For case 4, since A[mid] < target, then set i = mid+1. The loop terminates and both i and j point to 5.
# For all other cases, by the time the loop terminates, A[i] is not equal to 5. So we can easily know 5 is
# not in the sequence if the comparison fails.
# In conclusion, when the loop terminates, if A[i]==target, then i is the left boundary of the range;
# otherwise, just return -1;
# For the right of the range, we can use a similar idea. Again we can come up with several rules:
# If A[mid] > target, then the range must begin on the left of mid (j = mid-1)
# If A[mid] < target, then the range must begin on the right of mid (hence i = mid+1 for the next iteration)
# If A[mid] = target, then the range must begins on the right of or at mid (i= mid)
# Again, we can merge conditions 2 and 3 into:
# 2*. If A[mid] <= target, then i = mid;
# However, the terminate condition on longer works this time.
# Consider the following case:
# [5 7], target = 5
# Now A[mid] = 5, then according to rule 2), we set i = mid.
# This practically does nothing because i is already equal to mid.
# As a result, the search range is not moved at all!
# The solution is in using a small trick:
# Instead of calculating mid as mid = (i+j)/2, we now do:
# mid = (i+j)/2+1
# Why does this trick work?
# When we use mid = (i+j)/2, the mid is rounded to the lowest integer.
# In other words, mid is always biased towards the left. This means we could have i == mid when j - i == mid,
# but we NEVER have j == mid. So in order to keep the search range moving, we must make sure that the
# new i is set to something different than mid, otherwise we are at the risk that i gets stuck.
# But for the new j, it is okay if we set it to mid, since it was not equal to mid anyway.
# Our two rules in search for the left boundary happen to satisfy these requirements, so it works perfectly in that
# situation. Similarly, when we search for the right boundary,
# we must make sure i does not get stuck when we set the new i to i = mid.
# The easiest way to achieve this is by making mid biased to the right, i.e. mid = (i+j)/2+1.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        low = self.lowi(A, B)
        high = self.highi(A, B, len(A))
        return [low, high]

    def lowi(self, A, B):
        high = len(A) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == 0 or (mid > 0 and (A[mid - 1] != B))):
                return mid
            if A[mid] >= B:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def highi(self, A, B, n):
        high = len(A) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == n - 1 or (mid < n - 1 and (A[mid + 1] != B))):
                return mid
            if A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return -1
