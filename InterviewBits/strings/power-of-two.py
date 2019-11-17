"""
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.
Input:
number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:
return 1 if the number is a power of 2 else return 0
Example:
Input : 128
Output : 1
"""


# There is no shortcut to this problem.
# We need to divide the number by 2 till it is greater than 1.
# At any point, if the last digit is odd, then the number is not a power of 2.
# Lets see how we would implement division by 2.
# The division process is just the simulation of human division process.
# Start from the first digit. If the current digit is less than 2,
# then we append the next digit to current digit, and append 0 to our answer.

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n = int(A)
        if n == 1:
            return 0
        if n & (n - 1) == 0:  # That's cool
            return 1
        else:
            return 0

    def power_bin(self, A):
        m = bin(int(A))  # convert A to binary
        if m.count('1') == 1 and m[len(m) - 1] != '1':  # check if occurence is 1 and also last digit not equal to 1
            return 1
        else:
            return 0
