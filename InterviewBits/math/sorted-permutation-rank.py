"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.
Example :
Input : 'acb'
Output : 2
The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""


# If the first character is X, all permutations which had the first character less than X would
# come before this permutation when sorted lexicographically.
# Number of permutation with a character C as the first character =
# number of permutation possible with remaining N-1 character = (N-1)!
# rank = number of characters less than first character * (N-1)! + rank of permutation
# of string with the first character removed
# Example
# Lets say out string is “VIEW”.
# Character 1 : 'V'
# All permutations which start with 'I', 'E' would come before 'VIEW'.
# Number of such permutations = 3! * 2 = 12
# Lets now remove ‘V’ and look at the rank of the permutation ‘IEW’.
# Character 2 : ‘I’
# All permutations which start with ‘E’ will come before ‘IEW’
# Number of such permutation = 2! = 2.
# Now, we will limit our self to the rank of ‘EW’.
# Character 3:
# ‘EW’ is the first permutation when the 2 permutations are arranged.
# So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
# Hence, rank of permutation = 15.

class Solution:
    # @param A : string
    # @return an integer
    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n - 1)

    def findRank(self, A):
        res = 1
        for i in range(0, len(A) - 1):
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            res = (res + rank * self.fact(len(A) - i - 1)) % 1000003
        return res

# TODO: Should revisit to grasp completely.
