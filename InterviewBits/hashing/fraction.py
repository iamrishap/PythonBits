"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Example :
Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""


# Lets simulate the process of converting fraction to decimal. Lets look at the part where we have already
# figured out the integer part which is floor(numerator / denominator).
# Now you are left with ( remainder = numerator%denominator ) / denominator.
# If you remember the process of converting to decimal, at each step you do the following :
# 1) multiply the remainder by 10,
# 2) append remainder / denominator to your decimals
# 3) remainder = remainder % denominator.
# At any moment, if your remainder becomes 0, you are done.
# However, there is a problem with recurring decimals. For example if you look at 1/3, the remainder never becomes 0.
# Notice one more important thing.
# If you start with remainder = R at any point with denominator d, you will always get the same sequence of digits.
# So, if your remainder repeats at any point of time, you know that the digits between the last occurrence
# of R will keep repeating.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, numerator, denominator):
        result = ""
        if (numerator > 0 > denominator) or (numerator < 0 < denominator):
            result = "-"  # if any of numerator or denominator is negative starting final string with (-) negative sign
        n, d = abs(numerator), abs(denominator)
        result += str(n // d)  # adding Quotient to final string
        remainder = n % d  # remainder
        if remainder > 0:
            result += "."  # if remainder then add decimal point in final string
        hash_map = {}  # creating a hash table for storing the fractional value
        while remainder and remainder not in hash_map:
            hash_map[remainder] = len(result)
            remainder *= 10
            result += str(remainder // d)
            remainder %= d
        if remainder in hash_map:
            result = result[:hash_map[remainder]] + "(" + result[hash_map[remainder]:] + ")"
        return result
