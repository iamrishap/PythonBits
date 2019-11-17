"""
Implement atoi to convert a string to an integer.
Example :
Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
"""


# We only need to handle four cases:
# Discards all leading whitespaces
# Sign of the number
# Overflow
# Invalid input
# Detecting overflow gets tricky. You need to detect overflow before the number is about to overflow. So:
# If the number is positive and the current number is greater than MAX_INT/10,
# and you are about to append a digit, then certainly your number will overflow.
# If the current number = MAX_INT / 10, then based on the last digit, we can detect if the number will overflow.

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        sign = 1
        j = 0

        # Process potential spaces
        # Note: using the string "strip" method makes a copy
        # which we prefer to avoid to save memory
        while j < len(A) and A[j] == " ":
            j += 1

        # If there are only spaces, return 0
        if j == len(A):
            return 0

        # Process potential +/- sign
        if A[j] == "+":
            j += 1
        elif A[j] == '-':
            j += 1
            sign = -1

        # Process digits
        start = j
        while j < len(A) and A[j] in map(str, range(10)):  # or use .isnumeric()
            j += 1

        # If there are no digits, return 0
        if start == j:
            return 0

        r = sign * int(A[start:j])
        return max(-2147483648, min(r, 2147483647))


s = Solution()
print(s.atoi("9 2704"))
print(s.atoi(" 000191 3483AUBER1"))
