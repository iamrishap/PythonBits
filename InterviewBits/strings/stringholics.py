"""
You are given an array A consisting of strings made up of the letters ‘a’ and ‘b’ only.
Each string goes through a number of operations, where:
1.	At time 1, you circularly rotate each string by 1 letter.
2.	At time 2, you circularly rotate the new rotated strings by 2 letters.
3.	At time 3, you circularly rotate the new rotated strings by 3 letters.
4.	At time i, you circularly rotate the new rotated strings by i % length(string) letters.
Eg: String is "abaa"
1.	At time 1, string is "baaa", as 1 letter is circularly rotated to the back
2.	At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back
3.	At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back
4.	At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back
5.	At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back
After some units of time, a string becomes equal to it’s original self.
Once a string becomes equal to itself, it’s letters start to rotate from the first letter again (process resets). So,
if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be
it’s original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 109+7.
Note: Your solution will run on multiple test cases so do clear global variables after using them.
Input:
A: Array of strings.
Output:
Minimum time, where maximum number of strings are equal to their original self.
Constraints:
1 <= size(A) <= 10^5
1 <= size of each string in A <= 10^5
Each string consists of only characters 'a' and 'b'
Summation of length of all strings <= 10^7
Example:
Input
A: [a, ababa, aba]
Output
4
String 'a' is it's original self at time 1, 2, 3 and 4.
String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
String 'aba' is it's original self at time 2 and 4. (aba => baa => aba)
Hence, 3 strings are their original self at time 4.
"""


# The number of bits being rotated for each string goes in the series 1,1+2,1+2+3,1+2+3+4 etc.
# So for the ith operation, (i*(i+1))/2 bits are rotated.
# Find the smallest i for which you get the same string.
# Strings with same lengths may have different answers depending on the string.
# String 1010 takes 3 operations, while string 1001 takes 7 operations.
# But there is a catch, this wont always give you the minimum number of operations.
# Its possible that during rotation, you can get the original string before the number of bits
# rotated is a multiple of LEN.
# Example: S=> 100100
# Here, in 2 operations, we get the original string back.
# This takes place because the string is made up of recurring substrings.
# Assume string A to be 100
# S => AA
# Hence, over here our length S of string is the length of recurring substring A,
# so N*(N+1)/2 should be a multiple of length of A.
# Length of recurring substring can easily be found out using KMP algorithm in O(N) time complexity for each string.
# Find the minimum number of operations for each string, and take the LCM of all these values to get the answer.
# Handling of overflow for LCM should be handled by breaking the number down into factors, and then
# taking LCM (Not needed for languages that don’t have integer limit).
# Hence total time complexity is O(N).

class Solution:
    def gcd(self, A, B):
        if B > A:
            A, B = B, A
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        ans = 1
        for k in A:
            for i in range(1, 1000000000):
                if ((i * (i + 1)) // 2) % len(k) == 0:
                    ans = ((ans * i) // self.gcd(ans, i))
                    break
        return ans % 1000000007


# TODO: Can be revisited. Skipped without understanding.
