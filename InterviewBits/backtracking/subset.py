"""
"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse=True)
        res = []
        for i in range(len(A)):
            x = [A[i]]
            # Extends(not appends) by adding new entries
            # Each entry is adding in reverse order so higher order entries are created first
            res.extend([x + y for y in res])
            res.append(x)
        res.append([])
        res.reverse()
        return res


s = Solution()
print(s.subsets([1, 2, 3]))


# TODO: Revisit to remember this elegant way
