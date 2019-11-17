"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
Assume that there will only be one solution
Example:
given array S = {-1 2 1 -4},
and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""


# As stated in the earlier hint, the naive approach is to have 3 loops of i,j,k over the array.
# We then just track S[i]+S[j]+S[k] for the case when (S[i]+S[j]+S[k]-target) is minimum.
# The code for the same looks something like the following :
#   IF number of elements in S < 3
#     THEN return -1; // Invalid case
#   minDifference = abs(S[0] + S[1] + S[2] - target);
#   bestTillNow = S[0] + S[1] + S[2];
#   FOR i = 0 to size of S
#     FOR j = i + 1 to size of S
#       FOR k = j + 1 to size of S
#         newDiff = abs(S[i] + S[j] + S[k] - target)
#         IF newDiff < minDifference
#           minDifference = newDiff
#           bestTillNow = S[i] + S[j] + S[k]
#         END IF
#       END FOR
#     END FOR
#   END FOR
#   bestTillNow is my answer.
# However, as stated earlier this approach is O(N^3). Lets see if we can do better.
# Lets sort the array.
# When the array is sorted, try to fix the least integer by looping over it.
# Lets say the least integer in the solution is arr[i].
# Now we need to find a pair of integers j and k, such that arr[j] + arr[k] is closest to (target - arr[i]).
# To do that, let us try the 2 pointer approach.
# If we fix the two pointers at the end ( that is, i+1 and end of array ), we look at the sum.
# If the sum is smaller than the sum we need to get to, we increase the first pointer.
# If the sum is bigger, we decrease the end pointer to reduce the sum.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closest = None
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while k > j:
                threeSum = A[i] + A[j] + A[k]
                if threeSum == B:
                    return threeSum
                if closest is None or abs(B - threeSum) < abs(B - closest):
                    closest = threeSum
                if threeSum < B:
                    j += 1
                else:
                    k -= 1
        return closest
