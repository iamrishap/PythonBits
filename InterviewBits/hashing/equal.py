"""
Given an array A of integers, find the index of values that satisfy A + B = C + D,
where A,B,C & D are integers values in the array
Note:
1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1
2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.
Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2
S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:
Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
"""


# Continuing from the first hint,
# Hashing can provide one more level of optimization.
# Lets look at our bruteforce solution once more :
# Loop I = 1 to N :
#   Loop J = 1 to N :
#     Loop K = 1 to N:
#         Loop L = 1 to N:
#                if condition is true then update ans
#          endLoop;
#      endLoop;
#    endLoop;
# endLoop;
# Do we need a loop for L if we have hashed out the values ?
# We know that A[I] + A[J] = A[K] + A[L].
# If we know, I, J and K, then we can determine what A[L] should be.
# We can lookup the value A[L] = A[I] + A[J] - A[K] in a hashmap.
# The solution then becomes O(N^3) instead of O(N^4).
# Do note that we need to take care of duplicate values here.
# However, this might be a little slow as well. We are looking for something better.
# Can we use more space to optimize the solution ? How about hashing pairwise sums ( A[i] + A[J], A[K] + A[L] ) ?
# Loop i = 1 to N :
#     Loop j = i + 1 to N :
#         calculate sum
#         If in hash table any index already exist for sum then
#             try to find out that it is valid solution or not IF Yes Then update solution
#         update hash table
#     EndLoop;
# EndLoop;

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):

        """ Return matching indices or None """
        n = len(A)
        sums = {}
        res = []
        # Iterate pairs in lexicographical order
        for i in range(n - 1):
            for j in range(i + 1, n):
                s = A[i] + A[j]
                if s in sums:
                    k, l = sums[s]
                    if i != k and i != l and j != l:
                        # Here k < i necessarilly
                        if res:
                            res = min(res, [k, l, i, j])
                        else:
                            res = [k, l, i, j]
                else:
                    sums[s] = (i, j)  # smallest pair for this sum
        return res
