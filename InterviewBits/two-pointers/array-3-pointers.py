"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
**abs(x) is absolute value of x and is implemented in the following manner : **
      if (x < 0) return -x;
      else return x;
Example :
Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]
Output : 5
         With 10 from A, 15 from B and 10 from C.
"""


# Windowing strategy works here.
# Lets say the arrays are A,B and C.
#
# Take 3 pointers X, Y and Z
# Initialize them to point to the start of arrays A, B and C
# Find min of X, Y and Z.
# Compute max(X, Y, Z) - min(X, Y, Z).
# If new result is less than current result, change it to the new result.
# Increment the pointer of the array which contains the minimum.
# Note that we increment the pointer of the array which has the minimum, because our goal is to decrease
# the difference. Increasing the maximum pointer is definitely going to increase the difference.
# Increase the second maximum pointer can potentially increase the difference ( however,
# it certainly will not decrease the difference ).

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        pA = 0
        pB = 0
        pC = 0
        minmax = float("inf")
        while pA < len(A) and pB < len(B) and pC < len(C):
            minmax = min(minmax, max(abs(A[pA] - B[pB]), abs(B[pB] - C[pC]), abs(C[pC] - A[pA])))
            if A[pA] == min(A[pA], B[pB], C[pC]):
                pA += 1
            elif B[pB] == min(A[pA], B[pB], C[pC]):
                pB += 1
            else:
                pC += 1

        return minmax
