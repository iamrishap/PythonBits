"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :
Given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""


# Some elements can be repeated in the input set.
# Make sure you iterate over the number of occurrences of those elements to make sure you are not
# counting the same combinations again.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = set()

        def combinationSumHelper(arr, sumSoFar, index):
            if sumSoFar == B:
                ans.add(tuple(arr))
            elif sumSoFar > B:
                return
            else:
                for i in range(index, len(A)):
                    combinationSumHelper(arr + [A[i]], sumSoFar + A[i], i + 1)
        combinationSumHelper([], 0, 0)

        return list(ans)


# TODO: Revisit to understand
