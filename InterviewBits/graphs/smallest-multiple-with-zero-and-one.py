"""
You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only.
Since this multiple could be large, return it in form of a string.

Note:
Returned string should not contain leading zeroes.
For example,
For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
"""


class Solution:
    def multiple(self, A):
        flag = False
        i = 1
        while flag != True:
            result = A * i
            # method returns smallest  multiple which has binary digits
            allowed_chars = set('01')
            validationString = str(result)
            if set(validationString).issubset(allowed_chars):
                flag = True;
                break;
            else:
                i = i + 1
        return validationString
