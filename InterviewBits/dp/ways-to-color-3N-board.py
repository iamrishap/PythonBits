"""
Given a 3 x A board, find the number of ways to color it using at most 4 colors such that no
 2 adjacent boxes have same color.
Diagonal neighbors are not treated as adjacent boxes.
Return the ways modulo 109 + 7 as the answer grows quickly.
Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return an integer representing the number of ways to color the board.
Constraints:
1 <= A < 100000
Examples:
Input 1:
    A = 1
Output 1:
    36
Input 2:
    A = 2
Output 2:
    588
"""

# Let us first color a given column with three colors such that no two adjacent boxes have the same color.
# A simple combinatorics reveal that there are 36 ways to do so.
# Let’s say colors are: {0,1,2,3}
# Triplets of color: {0,1,2} , {3,1,2}, {4,1,2}, …..
# Now, suppose that we color the given column with one of these triplets. We acan color the next column
# with the triplets of color that do not contradict our coloring scheme.
# E.g.:
#   0	1
#  	1	3
#  	2	0
# Here, we can color third column using triplets that go well with the triplet {1,3,0}. These are {0,1,2}, {2,1,3}, ……
# This can be coded using a simple dynamic programming approach.
# Recurrence:
# {i,j,k} = triplet of color used to paint nth column in the order given. (1st row: i, 2nd row: j, …. }
# solve(i,j,k,n) = no. of ways to color a 3xn board such that nth column is painted with color triplet {i,j,k}
# solve(i,j,k,n) =$\sum_{triplets(x,y,z)}$ ( solve(x,y,z, n-1) ) such that {i,j,k} and {x,y,z} go well with each other.


from itertools import product


def count(x, y, z):
    ''' number of ways to form 2 and 3-colored column '''
    ''' x, y, z = colors of previous column '''
    num2, num3 = 0, 0
    for a, b, c in product(range(4), repeat=3):
        if a != b and b != c and a != x and b != y and c != z:
            if a == c:
                num2 += 1
            else:
                num3 += 1
    return num2, num3


class Solution:
    def solve_another(self, A):
        # ways to fill first column
        c3 = 24  # when 3 colors (A,B,C,D) used: 4*3*2
        c2 = 12  # when 2 colours (A,B,C) used: 4*3
        # ways to fill 2nd column onwards
        for i in range(2, A + 1):
            temp = c3
            c3 = (11 * c3 + 10 * c2) % 1000000007  # calculated manually
            c2 = (5 * temp + 7 * c2) % 1000000007
        return (c3 + c2) % 1000000007

    # @param A : integer
    # @return an integer
    def solve(self, A):
        MODU = 1000000007
        if A == 0:
            return 1
        # First column
        n2, n3 = count(None, None, None)  # 12, 24
        # When previous column has 2 colors (resp. 3)
        n2_2, n2_3 = count(0, 1, 0)  # 7, 10
        n3_2, n3_3 = count(0, 1, 2)  # 5, 11
        # n2, n3: number of combinations ending with 2 colored column (resp. 3)
        for i in range(1, A):
            n2, n3 = (n2 * n2_2 + n3 * n3_2) % MODU, \
                     (n2 * n2_3 + n3 * n3_3) % MODU
        return (n2 + n3) % MODU
