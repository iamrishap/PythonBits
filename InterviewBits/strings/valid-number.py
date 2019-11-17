"""
Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.
Please think of all the corner cases and clarifications yourself.
Validate if a given string is numeric.
Examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Clarify the question using “See Expected Output”
Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem
"""


# This is a brute force problem with lot of corner cases. You need to properly figure them out before coding.
# Some of them includes dealing with numbers having different signs.
# To start with, make sure you skip the whitespaces.
# Then ignore the ‘+’ or ‘-‘ sign.
# Scan the following string till you find numbers and ‘.’ and confirm at least one digit, less than one ‘.’
# and the string not ending with ‘.’.
# Now the remaining string could have ‘e’ followed by a number.
# Confirm if the next character is ‘e’, then again repeat the process of skipping the sign and looking for digits.

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        while len(A) > 0 and A[0] == ' ':
            A = A[1:]
        A = A[::-1]
        while len(A) > 0 and A[0] == ' ':
            A = A[1:]
        A = A[::-1]
        if len(A) == 0:
            return 0
        for c in A:
            if c not in [str(i) for i in range(10)] + ['.', 'e', '-', '+']:
                return 0
        if 'e' in A:
            A = A.split('e')
            if len(A) != 2:
                return 0
            return int(self.isnum(A[0], 0) and self.isnum(A[1], 1))
        return int(self.isnum(A, 0))

    def isnum(self, A, i):
        # print(A,i)
        if A == '':
            return False
        if i == 1 or (i == 0 and '.' not in A):
            if A[0] in ['+', '-']:
                A = A[1:]
            if A == '':
                return False
            for c in A:
                if c not in [str(i) for i in range(10)]:
                    return False
            return True
        A = A.split('.')
        return (self.isnum(A[0], 1) or A[0] == '') and self.isnum(A[1], 1)

    def isNumber_re(self, A):
        import re
        p = re.compile(r"^\s*[+-]?\d+(\.\d+)?(e[-+]?\d+)?\s*$")
        if (p.match(A)):
            return 1
        p = re.compile(r"^\s*[+-]?\.\d+(e[-+]?\d+)?\s*$")
        if (p.match(A)):
            return 1
        return 0


s = Solution()
print(s.isNumber_re("2e10"))
