"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example:
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# This is a fairly simple question.
# You need to maintain 2 pointers, one from the beginning and one from the end.
# At every iteration, after skipping the non alphanumeric characters, both the characters should match.


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start < end:
            if A[start].isalnum() and A[end].isalnum():
                ast = A[start].lower()
                aen = A[end].lower()
                if ast != aen:
                    return 0
                else:  # One more matching pair processed
                    start += 1
                    end -= 1
            elif not A[start].isalnum():
                start += 1
            elif not A[end].isalnum():
                end -= 1
        return 1
