"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi
AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
"""


# In every recursion run, you either include the element in the combination or you don’t.
# To account for multiple occurrences of an element, make sure you call the next function without
# incrementing the current index.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = sorted(list(set(A)))

        def rec(A, s):
            if len(A) == 0: return []
            if s < 0: return []
            if s == 0: return [[]]
            aux = rec(A[1:], s)
            aux2 = rec(A[0:], s - A[0])
            for i in range(len(aux2)):
                aux2[i] = [A[0]] + aux2[i]
            return aux + aux2
        return sorted(rec(A, B))

# TODO: Revisit to understand
