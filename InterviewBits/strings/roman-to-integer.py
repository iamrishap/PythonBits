"""
Given a string A representing a roman numeral.
Convert A into integer.
A is guaranteed to be within the range from 1 to 3999.
Input Format
The only argument given is string A.
Output Format
Return an integer which is the integer verison of roman numeral string.
For Example
Input 1:
    A = "XIV"
Output 1:
    14
Input 2:
    A = "XX"
Output 2:
    20
"""


# Note how the number XVI(10+5+1) and XIV(10-1+5) differs.
# In one case we are adding the numeric value of a letter and in other case we are subtracting it.
# How can you simulate this?
# The key is to notice that in a valid Roman numeral representation the letter
# with the most value always occurs at the start of the string.
# Whenever a letter with lesser value precedes a letter of higher value,
# it means its value has to be added as negative of that letter’s value. In all other cases, the values get added.

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        # I V X  L  C   D   M
        # 1 5 10 50 100 500 1000
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        n = len(A)
        r = 0
        if n == 0:
            return 0
        if n == 1:
            return d[A[0]]
        for i in range(1, n):
            a = d[A[i - 1]]
            b = d[A[i]]
            if a >= b:  # If the last digit was bigger
                r += a
            else:
                r -= a
        r += d[A[n - 1]]  # Adding the final digit
        return r
