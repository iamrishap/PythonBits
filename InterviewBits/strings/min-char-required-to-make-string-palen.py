"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.
Input Format
The only argument given is string A.
Output Format
Return the minimum characters that are needed to be inserted to make the string a palindrome string.
For Example
Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".
Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".
"""


# Each index of LPS array contains the longest prefix which is also a suffix. Now take the string and reverse of a
# string and combine them with a sentinal character in between them and compute the LPS array of this combined string.
# Now take the last value of the LPS array and subtract it with the length of the original string, This will give us
# the minimum number of insertions required in the begining of the string .

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        while A != A[::-1]:
            A = A[:-1]  # Remove the last char
            count += 1
        return count


s = Solution()
print(s.solve("AAABCA"))
