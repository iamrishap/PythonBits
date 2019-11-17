"""
Reverse digits of an integer.
Example1:
x = 123,
return 321
Example2:
x = -123,
return -321
Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""


# Here are some good questions to ask before coding.
# If the integer’s last digit is 0, what should the output be? ie, cases such as 10, 100.
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse
# of 1000000003 overflows. How should you handle such cases?
# Tips:
# 1) num % 10 gives you the last digit of a number.
# 2) num / 10 gives you the number after removing the last digit.
# 3) num * 10 + digit appends the digit at the end of the number.

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if int(A) > 0:
            k = int(str(A)[::-1])
            return k * (k < 2 ** 31)
        else:
            k = -1 * int(str(A)[1:][::-1])
            return k * (k > -2 ** 31)

    def reverse_another(self, A):
        sgn = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2 ** 31 - 1:
            return 0
        return sgn * result


s = Solution()
print(s.reverse("1000000003"))
