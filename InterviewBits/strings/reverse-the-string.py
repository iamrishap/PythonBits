"""
Given a string A.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
Input Format
The only argument given is string A.
Output Format
Return the string A after reversing the string word by word.
For Example
Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"
Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
"""


# One simple approach is a two-pass solution:
# First pass to split the string by spaces into an array of words
# Then second pass to extract the words in reversed order
# We can do better in one-pass. While iterating the string in reverse order,
# we keep track of a word’s beginning and end position.
# When we are at the beginning of a word, we append it.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        flag = 0
        for i in range(len(A)):
            if A[i] == " ":
                flag = 1
                break
        if flag == 0:
            return A
        start = 0
        last = 0
        s = ""
        while last < len(A):
            if A[last] == " ":  # Found a word between start and last
                start += 1
                last += 1
                if last == len(A) - 1 and A[last] != " ":
                    s = A[start:last + 1] + " " + s
            if A[last] != " ":
                last += 1
                if last < len(A):
                    if A[last] == " ":
                        s = A[start:last] + " " + s
                        start = last  # For the next word
                        continue
                    if last == len(A) - 1:
                        s = A[start:last + 1] + " " + s
        return s[:len(s) - 1]

    def solve_easy(self, a):
        l = a.split()
        l.reverse()
        return ' '.join(l)


s = Solution()
print(s.solve("the sky is blue"))
