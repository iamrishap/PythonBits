"""
Given a collection of numbers, return all possible permutations.
Example:
[1,2,3] will have the following permutations:
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
"""


# Lets say we are at index start then we can swap element at this index with any index>start and permute the
# elements starting from start+1 using recursion. You can swap back the elements at start and index in order
# to maintain the order for next recursive call.

class Solution:

    def helper(self, res, cur, A):
        if not A:  # A == [] # If we've exhausted the array, we would've got a permutation. Append it to result.
            res.append(cur)
            return
        for i in range(len(A)):
            self.helper(res, cur + [A[i]], A[:i] + A[i + 1:])

    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res = []
        self.helper(res, [], A)
        return res


s = Solution()
print(s.permute([1, 2, 3]))

# TODO: Revise as it is frequently asked
