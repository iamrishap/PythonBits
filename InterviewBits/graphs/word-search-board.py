"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
The same letter cell may be used more than once.

Example :
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0
Note that 1 corresponds to true, and 0 corresponds to false.
"""


class Solution:
    def exist(self, A, B):
        if not A:
            return 0 if B else 1

        m, n, s = len(A), len(A[0]), len(B)

        def helper(i, j, k=0, memo={}):
            # return whether B[k:] fit from (i, j) starting point
            if k == s:
                return True
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if 0 <= i < m and 0 <= j < n and B[k] == A[i][j]:
                res = helper(i - 1, j, k + 1) or \
                      helper(i + 1, j, k + 1) or \
                      helper(i, j - 1, k + 1) or \
                      helper(i, j + 1, k + 1)
            else:
                res = False

            memo[(i, j, k)] = res
            return res

        for i in range(m):
            for j in range(n):
                if helper(i, j):
                    return 1

        return 0

A = [
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
s = Solution()
print(s.exist(A, "ABCCED"))
print(s.exist(A, "SEE"))
print(s.exist(A, "ABCB"))
print(s.exist(A, "ABFSAB"))
print(s.exist(A, "ABCD"))
