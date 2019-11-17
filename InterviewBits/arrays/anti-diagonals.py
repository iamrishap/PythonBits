"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:
Input:
1 2 3
4 5 6
7 8 9
Return the following :
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
Input :
1 2
3 4
Return the following  :
[
  [1],
  [2, 3],
  [4]
]
"""
class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        B = [[] for i in range(len(a)*2)]
        # Done smoothly
        for i in range(len(a)):
            for j in range(len(a)):
                B[i+j].append(a[i][j])
        return B[:-1]


A = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.diagonal(A)
