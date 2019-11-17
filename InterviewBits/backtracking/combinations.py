"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
Make sure the combinations are sorted.
To elaborate,
Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        return self.x(1, A, B)

    def x(self, start, end, length):
        if length == 0:
            return [[]]  # only one combination for k=0
        if end - start + 1 < length:
            return []  # no combination possible
        result = []
        for i in range(start, end + 1):  # Pick each element as the start
            for e in self.x(i + 1, end, length - 1):  # This does the core operation
                result.append([i] + e)
        return result


s = Solution()
print(s.combine(5, 3))

# TODO: Revisit to revise
