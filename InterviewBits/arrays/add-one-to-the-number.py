"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = int(''.join([str(val) for val in A])) + 1
        return [int(val) for val in str(num)]

    def plusOne_editorial(self, A):
        val = 1;
        for i in range(len(A), 0, -1):
            val = val + A[i - 1]
            borrow = int(val / 10)
            if borrow == 0:
                A[i - 1] = val
                break;
            else:
                A[i - 1] = val % 10
                val = borrow
        A = [borrow] + A  # Not sure what this does!
        while A[0] == 0:
            del A[0]
        return A


s = Solution()
print(s.plusOne([1, 2, 3, 4]))
print(s.plusOne([0, 0, 1, 2, 3, 4]))
