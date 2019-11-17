"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""


# This is very similar to the problem where you need to generate subsets for distinct integer.
# However, in this case, because of repetitions, things are not as simple as choosing or rejecting an element.
# Now for the  elements which are repeated you need to iterate over the count of elements
# you are going to include in your subset.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        ans = []
        A.sort()

        def solution(A, sub_set, i):
            ans.append(sub_set)
            for j in range(i, len(A)):
                if i != j and A[j - 1] == A[j]:
                    continue
                solution(A, sub_set + [A[j]], j + 1)

        solution(A, [], 0)
        return ans

# TODO: Revisit to understand
