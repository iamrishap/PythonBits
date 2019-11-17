"""
Please Note:
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version
 Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all
 the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question,
 https://projecteuler.net/about=roman_numerals has very detailed explanations.
Input Format
The only argument given is integer A.
Output Format
Return a string denoting roman numeral version of A.
Constraints
1 <= A <= 3999
For Example
Input 1:
    A = 5
Output 1:
    "V"
Input 2:
    A = 14
Output 2:
    "XIV"
"""


# It is very much like learning our own number system.
# All you need to know is how to write 0-9, 10, 20, 30, 40, .. 90, 100, 200, 300,… 900, 1000, 2000, 3000.
# You can derive rest of the numbers using the above.

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        s = ""
        num = A
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        i = 0
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        while num > 0:
            for x in range(num // val[i]):
                s = s + syb[i]  # Add roman
                num = num - val[i]  # Reduce integer
            i = i + 1  # Controls the steps
        return s
