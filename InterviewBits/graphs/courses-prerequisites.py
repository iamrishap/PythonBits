"""
There are a total of A courses you have to take, labeled from 1 to A.
Some courses may have prerequisites, for example to take course 2 you have to first take course 1,
which is expressed as a pair: [1,2].
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

Input Format:
The first argument of input contains an integer A, representing the number of courses.
The second argument of input contains an integer array, B.
The third argument of input contains an integer array, C.
Output Format:
Return a boolean value:
    1 : If it is possible to complete all the courses.
    0 : If it is not possible to complete all the courses.
Constraints:

1 <= A <= 6e4
1 <= length(B) = length(C) <= 1e5
1 <= B[i], C[i] <= A
Example:

Input 1:
    A = 3
    B = [1, 2]
    C = [2, 3]

Output 1:
    1

Explanation 1:
    It is possible to complete the courses in the following order:
        1 -> 2 -> 3

Input 2:
    A = 2
    B = [1, 2]
    C = [2, 1]

Output 2:
    0

Explanation 2:
    It is not possible to complete all the courses.
"""

# Assume the non-visited node are colored black, the nodes currently present in the recursion stack are colored blue and
# the nodes already visited and out of the recursion stack are colored grey. The edge that connects current
# vertex in DFS to the vertex in the recursion stack(blue coloured node) is back edge.


from collections import defaultdict
from queue import LifoQueue


class Solution:
    def solve(self, A, B, C):
        G = defaultdict(list)
        # Convert to a graph format
        for a, b in zip(B, C):
            G[a].append(b)
        # C = {}  # Checked nodes. Useful for processing disconnected graphs.
        C = set()
        # K = 1
        for i in range(1, A + 1):
            if i not in C:  # If the graph is not connected, we need to make sure all nodes are visited
                visited = defaultdict(bool)
                S = LifoQueue()  # Stack for DFS
                S.put(i)
                visited[i] = True
                while not S.empty():
                    n = S.get()
                    for neighbour in G[n]:  # Visit all neighbours
                        if visited[neighbour]:
                            return 0
                        else:
                            visited[neighbour] = True
                            S.put(neighbour)
                    C.add(n)
                    # C[n] = K  # Checked
                    # K += 1
        return 1


A = 3
B = [1, 2]
C = [2, 3]
s = Solution()
print(s.solve(A, B, C))
