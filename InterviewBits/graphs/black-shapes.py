"""
Given N x M character matrix A of O's and X's, where O = white, X = black.
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
Input Format:
The First and only argument is a N x M character matrix.
Output Format:
Return a single integer denoting number of black shapes.
Constraints:
1 <= N,M <= 1000
A[i][j] = 'X' or 'O'
Example:
Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.
XXX
XXX
XXX
is just one single connected black shape.
"""


class Solution:
    def black(self, A):
        def dfs(A, i, j, final):
            xarr = [-1, 0, 1, 0]
            yarr = [0, 1, 0, -1]
            for k in range(4):
                x = i + xarr[k]
                y = j + yarr[k]
                if (x, y) not in final:
                    if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 'X':
                        final.add((x, y))
                        dfs(A, x, y, final)
        ans = 0
        final = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X' and (i, j) not in final:
                    final.add((i, j))
                    dfs(A, i, j, final)
                    ans += 1
        return ans


A = [
    'OOOXOOO',
    'OOXXOXO',
    'OXOOOXO'
]

s = Solution()
print(s.black(A))
