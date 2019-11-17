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

# Sort both the arrays in ascending order.
# Let us take priority queue (heap).
# First max element is going to be the sum of the last two elements of array A and B i.e. (A[n-1] + B[n-1]).
# Insert that in heap with indices of both array i.e (n-1, n-1).
# Start popping from heap (n-iterations).
# And insert the sum (A[L-1]+A[R]) and (A[L]+B[R-1]).
# Take care that repeating indices should not be there in the heap (use map for that).

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
