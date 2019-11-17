"""
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of
triangles which you can form using these array values.
Notes:
You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter.
Any triangle formed should have a positive area.
Return answer modulo 109 + 7.
For example,
A = [1, 1, 1, 2, 2]
Return: 4
"""


# First we sort the array of side lengths. So since Ai < Aj < Ak where i < j < k,
# therefore it is sufficient to check Ai + Aj > Ak to prove they form a triangle.
# Thus for every i and j, we can find the maximum value of k such that the triangle inequality holds.
# Also we can also prove that for every such index i, we only have to increase the value of the
# k (satisfying the above condition) for every iteration of j from i+1 to n. Therefore, we get a O(n2)
# solution (Proof of this is left to the reader).

class Solution:
    # @param A : list of integers
    # @return an integer

    def nTriang(self, A):
        n = len(A)
        A.sort()
        count = 0
        for i in range(0, n - 2):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and A[i] + A[j] > A[k]:
                    k += 1
                count += k - j - 1

        return count % 1000000007

    def nTriang_another(self, A):
        A.sort(reverse=True)
        t = 0
        for i in range(0, len(A) - 2):
            third_side = A[i]
            j = i + 1
            k = len(A) - 1
            while j < k:
                if A[j] + A[k] > third_side:
                    t += (k - j)
                    j += 1
                else:
                    k -= 1
        return t % (10 ** 9 + 7)
