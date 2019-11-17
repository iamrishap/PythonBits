"""
Given a string S, find the longest palindromic substring in S.
Substring of string S:
S[i...j] where 0 <= i <= j < len(S)
Palindrome string:
A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first ( with the least starting index ).
Example :
Input : "aaaabaaa"
Output : "aaabaaa"
"""

# A common mistake:
#
# Some people will be tempted to come up with a quick solution,
# which is unfortunately flawed (however can be corrected easily):
#  Reverse S and become S’. Find the longest common substring between S and S’,
#  which must also be the longest palindromic substring.
# This seemed to work, let’s see some examples below.
# For example,
# S = “caba”
# S’ = “abac”
# The longest common substring between S and S’ is “aba”, which is the answer.
# Let’s try another example:
# S = “abacdfgdcaba”
# S’ = “abacdgfdcaba”
# The longest common substring between S and S’ is “abacd”. Clearly, this is not a valid palindrome.
# We could see that the longest common substring method fails when there exists a reversed copy of a
# non-palindromic substring in some other part of S. To rectify this, each time we find a longest common
# substring candidate, we check if the substring’s indices are the same as the reversed substring’s original
# indices. If it is, then we attempt to update the longest palindrome found so far; if not,
# we skip this and find the next candidate.
# This gives us a O(N2) DP solution which uses O(N2) space (could be improved to use O(N) space).
# Please read more about Longest Common Substring here.
# Brute force solution, O(N3):
# The obvious brute force solution is to pick all possible starting and ending positions for a substring,
# and verify if it is a palindrome. There are a total of C(N, 2) such substrings (excluding the
# trivial solution where a character itself is a palindrome).
# Since verifying each substring takes O(N) time, the run time complexity is O(N3).
# Dynamic programming solution, O(N2) time and O(N2) space:
# To improve over the brute force solution from a DP approach, first think how we can avoid unnecessary
# re-computation in validating palindromes. Consider the case “ababa”. If we already knew that “bab” is a
# palindrome, it is obvious that “ababa” must be a palindrome since the two left and right end letters are the same.
# Stated more formally below:
# Define P[ i, j ] ← true iff the substring Si … Sj is a palindrome, otherwise false.
# Therefore,
# P[ i, j ] ← ( P[ i+1, j-1 ] and Si = Sj )
# The base cases are:
# P[ i, i ] ← true
# P[ i, i+1 ] ← ( Si = Si+1 )
# This yields a straight forward DP solution, which we first initialize the one and two letters palindromes,
# and work our way up finding all three letters palindromes, and so on…
# Can you come up with a O(N^2) time complexity and O(1) space solution ?
# A simpler approach, O(N2) time and O(1) space:
# In fact, we could solve it in O(N2) time without any extra space.
# We observe that a palindrome mirrors around its center.
# Therefore, a palindrome can be expanded from its center, and there are only 2N-1 such centers.
# You might be asking why there are 2N-1 but not N centers?
# The reason is that the center of a palindrome can be in between two letters.
# Such palindromes have even number of letters (such as “abba”) and their center are between the two ‘b’s.
# Since expanding a palindrome around its center could take O(N) time, the overall complexity is O(N2).

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return A
        cs = 2 * n - 1
        ans = ''
        for c in range(cs):
            i = int(c / 2)  # Elegantly done
            j = i
            if c % 2 != 0:  # Using different i and j for palindrome center with 2 characters
                i = i + 1
            while i < n and j >= 0 and A[i] == A[j]:
                if len(ans) < i - j + 1:
                    ans = A[j:i + 1]
                i += 1
                j -= 1

        return ans


s = Solution()
print(s.longestPalindrome("aaaabaaa"))
