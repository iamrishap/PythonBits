"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible
that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move
outside the boundary of the rectangle at any point of time.

Input Format

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO
Explanation:
    There is NO valid path in this case
"""


class Solution:

    def notInCircle(self, r, E, F, y, x):
        # E, F will have the x, y coordinates of all the circles
        for z in range(len(E)):
            if ((E[z] - x) ** 2 + (F[z] - y) ** 2) ** 0.5 <= r:
                return False
        return True

    def solve(self, A, B, C, D, E, F):
        stack = []
        graph = [[False] * (A + 1) for _ in range(B + 1)]
        stack.append([0, 0])
        while stack:
            curr = stack.pop()
            if curr[0] + 1 <= B and not graph[curr[0] + 1][curr[1]]  \
                    and self.notInCircle(D, E, F, curr[0] + 1, curr[1]):
                stack.append([curr[0] + 1, curr[1]])
                graph[curr[0] + 1][curr[1]] = True
            if curr[0] - 1 >= 0 and not graph[curr[0] - 1][curr[1]] \
                    and self.notInCircle(D, E, F, curr[0] - 1, curr[1]):
                stack.append([curr[0] - 1, curr[1]])
                graph[curr[0] - 1][curr[1]] = True
            if curr[1] + 1 <= A and not graph[curr[0]][curr[1] + 1] \
                    and self.notInCircle(D, E, F, curr[0], curr[1] + 1):
                stack.append([curr[0], curr[1] + 1])
                graph[curr[0]][curr[1] + 1] = True
            if curr[1] - 1 >= 0 and not graph[curr[0]][curr[1] - 1] \
                    and self.notInCircle(D, E, F, curr[0], curr[1] - 1):
                stack.append([curr[0], curr[1] - 1])
                graph[curr[0]][curr[1] - 1] = True
        if graph[B][A]:
            return 'YES'
        else:
            return 'NO'


s = Solution()
print(s.solve(2, 3, 1, 1, [3], [3]))
