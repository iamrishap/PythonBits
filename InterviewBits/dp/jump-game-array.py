"""
Given an array of non-negative integers, A, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Input Format:
The first and the only argument of input will be an integer array A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
    => 0 : If you cannot reach the last index.
    => 1 : If you can reach the last index.
Constraints:
1 <= len(A) <= 1e6
0 <= A[i] <= 30
Examples:
Input 1:
    A = [2,3,1,1,4]
Output 1:
    1
Explanation 1:
    Index 0 -> Index 2 -> Index 3 -> Index 4 -> Index 5
Input 2:
    A = [3,2,1,0,4]
Output 2:
    0
Explanation 2:
    There is no possible path to reach the last index.
"""


# Note that from an index i, you can choose to jump to any index in the range [i, i+A[i]].
# Now if there is at least one index in the said range from where it is possible to jump to the end index, we are done.
# So if we start solving from end to start, and for every i, we loop j from i to i + A[i], and check if a
# solution is possible for j, then solution is possible for i.
# This approach is however not linear. Take a moment and try to think if you can reduce this to O(n) approach.
# To move to linear approach, just maintain the minimum index which has solution possible till now.
# If its less than i+A[i]], then solution is possible for i and the minimum index gets updated to i.
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        chk = [i for i in A]
        print(chk)
        for i in range(len(A) - 1):
            for j in range(i + 1, min(i + A[i] + 1, len(A))):
                chk[j] += A[i] - (j - i)  # What is this trying to do??
        print(chk)
        for i in range(len(chk)):
            if chk[i] == 0 and i != len(chk) - 1:  # Any unreachable position, except end
                return 0
        return 1


A = [3, 2, 1, 0, 4]
s = Solution()
print(s.canJump(A))


# TODO: Don't know what the marked line does!!!
