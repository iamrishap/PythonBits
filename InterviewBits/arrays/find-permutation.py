"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of
first n positive integer that satisfy the given input string.
D means the next number is smaller, while I means the next number is greater.
Notes:
Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :
Input 1:
n = 3
s = ID
Return: [1, 3, 2]
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        mn, mx = 1, B
        result = []
        for x in A:
            if x == 'D':
                result.append(mx)
                mx -= 1
            elif x == 'I':
                result.append(mn)
                mn += 1
        result.append(mn)
        return result


s = Solution()
print(s.findPerm('DIDD', 5))
