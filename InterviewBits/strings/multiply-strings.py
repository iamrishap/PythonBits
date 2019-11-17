"""
Given two numbers represented as strings, return multiplication of the numbers as a string.
 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.
NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a string = A*B
    def multiply(self, A, B):
        # School multiplication implemented
        # max no. of digits result can have
        ans = ['0'] * (len(A) + len(B) + 1)
        pos = 0  # rightmost in ans at curr level
        for i in range(len(B)):
            k = int(B[-(i + 1)])
            carr = 0  # carry
            pos -= 1  # putting a cross on right
            for j in range(len(A)):
                temp = k * int(A[-(j + 1)]) + int(ans[pos - j]) + carr
                ans[pos - j] = str(temp % 10)
                carr = temp / 10
            ans[pos - len(A)] = str(carr)
        ret = ''.join(ans).lstrip('0')
        if ret == '':
            ret = '0'
        return ret
