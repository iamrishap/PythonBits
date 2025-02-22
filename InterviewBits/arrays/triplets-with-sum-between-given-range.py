"""
Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.
Example:
Given [0.6, 0.7, 0.8, 1.2, 0.4] ,
You should return 1
as
0.6+0.7+0.4=1.7
1<1.7<2
Hence, the output is 1.
O(n) solution is expected.
Note: You can assume the numbers in strings don’t overflow the primitive data type and
there are no leading zeroes in numbers. Extra memory usage is allowed.
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
        for i in range(3, n):
            if 1 < (a + b + c) < 2:
                return 1
            elif (a + b + c) > 2:
                # If overflow, replace the max
                if a > b and a > c:
                    a = float(A[i])
                elif b > a and b > c:
                    b = float(A[i])
                elif c > a and c > b:
                    c = float(A[i])
            else:
                # If underflow, replace the min
                if a < b and a < c:
                    a = float(A[i])
                elif b < a and b < c:
                    b = float(A[i])
                elif c < a and c < b:
                    c = float(A[i])
        return 1 if 1 < (a + b + c) < 2 else 0


s = Solution()
print(s.solve([0.6, 0.7, 0.8, 1.2, 0.4]))
