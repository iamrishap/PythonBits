"""
Max Non Negative SubArray
Asked in:
Google
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
1 <= A[i] <= 1e5
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Approach: Maintain 2 dictionaries with values of the start index, end index,
    # sum and length for the current and max
    # Append(-1) to avoid handling end of array separately
    def maxset(self, A):
        # Edge case
        if len(A) == 1:
            return A if A[0] > 0 else []

        A.append(-1)
        # Dict to store various useful intermediary values to reach the solution
        val_now = {
            'inx_low': -1,
            'inx_high': -1,
            'sum': 0,
            'len': 0
        }
        val_max = val_now.copy()

        for idx, val in enumerate(A):
            if val > -1:
                if val_now['inx_low'] == -1:
                    val_now['inx_low'] = idx
                val_now['sum'] += val
                val_now['len'] += 1
            else:
                # Encountered first -ve value
                if val_now['inx_low'] != -1:   # If `val_now` is set
                    val_now['inx_high'] = idx - 1 # Set `ind_high`
                    if val_now['sum'] > val_max['sum'] or \
                            (val_now['sum'] == val_max['sum'] and val_now['len'] > val_max['len']):
                        val_max = val_now.copy()

                    # Reset `val_now`
                    val_now['sum'] = val_now['len'] = 0
                    val_now['inx_low'] = val_now['inx_high'] = -1
                # Consecutive -ve value found
                else:
                    pass  # Do nothing
        return A[val_max['inx_low']: val_max['inx_high'] + 1]

    # Approach: Maintain just indices with values of the start index, end index, sum and length for the current and max
    # Edge cases don't need to be handled separately
    def maxset_billbezos(self, A):
        s, j = 0, 0
        a, b, max_s = 0, -1, 0
        A.append(float('-inf'))
        for i in range(len(A)):
            if A[i] < 0:
                if s > max_s or (s == max_s and i - j > b - a):
                    a, b, max_s = j, i - 1, s
                j, s = i + 1, 0
            else:
                s += A[i]
        return A[a:b + 1]

s = Solution()
print(s.maxset([1, 2, 5, -7, -18, 2, 3, 8]))
print(s.maxset_billbezos([1, 2, 5, -7, -18, 2, 3, -3, 8]))
