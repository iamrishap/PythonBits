"""
N max pair combinations
Asked in:
Liv.ai
Problem Setter: dhruvi Problem Tester: ganeshk2
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)
"""

import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        visited = set()
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)
        result = []
        heap = []
        visited.add((0, 0))
        heapq.heappush(heap, (-(A[0] + B[0]), (0, 0)))
        for _ in range(N):
            sum, (iA, iB) = heapq.heappop(heap)
            result.append(-sum)

            tuple1 = (iA + 1, iB)
            if iA < N - 1 and tuple1 not in visited:
                heapq.heappush(heap, (-(A[iA + 1] + B[iB]), tuple1))
                visited.add(tuple1)

            tuple2 = (iA, iB + 1)
            if iB < N - 1 and tuple2 not in visited:
                heapq.heappush(heap, (-(A[iA] + B[iB + 1]), tuple2))
                visited.add(tuple2)

        return result


s = Solution()
print(s.solve([1, 2], [3, 4]))

# A : [ 36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0, 37, -42, 26, 28 ]
# B : [ 38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22, -9, 0, 43 ]
#
# 97 95 94 92 92 91 90 89 86 85 85 83 83 81 81 80 79 77 76 75 72 72 71 69 69 68 67 66 66 66 66 63 62 61 61 61 58 57 56 55 55 49 48 45 44 42 41 39 36 35 35 34 34 33 29 28 28 28 28 26 26 25 25 25 24 23 23 22 21 20 20 18 14 14 13 12 12 10 10 7 4 4 1
# 97 95 95 95 95 94 94 93 93 93 93 92 92 92 92 92 92 92 91 91 91 91 90 90 90 90 90 90 90 90 90 90 89 89 89 89 89 89 89 89 88 88 88 88 88 88 88 88 87 87 87 87 87 87 87 87 87 86 86 86 86 86 86 86 86 85 85 85 85 85 85 85 85 84 84 84 84 84 84 84 84 84 84
#
#
# A : [ 3, 2, 4, 2 ]
# B : [ 4, 3, 1, 2 ]
# Your function returned the following :
# 8 7 6 5
# The expected returned value :
# 8 7 7 6
