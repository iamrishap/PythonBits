"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 3
Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]
Input 2:
    4
Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
"""


class Direction(object):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class Solution:
    # @param A :
    # @return a list of integers
    def generateMatrix(self, A):
        result = [[0] * A for _ in range(A)]
        t, b, l, r = 0, A - 1, 0, A - 1
        direction = Direction.EAST
        lastN = 1
        while t <= b and l <= r:
            if direction is Direction.EAST:
                # A[t][l:r + 1]
                for col in range(l, r + 1):
                    result[t][col] = lastN
                    lastN += 1
                t += 1
            elif direction is Direction.SOUTH:
                # A[r][t:b + 1]
                for row in range(t, b + 1):
                    result[row][r] = lastN
                    lastN += 1
                r -= 1
            elif direction is Direction.WEST:
                # reversed(A[b][l:r + 1])
                for col in reversed(range(l, r + 1)):
                    result[b][col] = lastN
                    lastN += 1
                b -= 1
            elif direction is Direction.NORTH:
                for row in reversed(range(t, b + 1)):
                    result[row][l] = lastN
                    lastN += 1
                l += 1
            direction = (direction + 1) % 4
        return result


s = Solution()
print(s.generateMatrix(4))
