"""
Given a number A, return number of ways you can draw A chords in a circle
with 2 x A points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.
Return the answer modulo 109 + 7.
Input Format:
The first and the only argument contains the integer A.
Output Format:
Return an integer answering the query as described in the problem statement.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 1
Output 1:
    1
Explanation 1:
    If points are numbered 1 to 2 in clockwise direction, then different ways to draw chords are:
    {(1-2)} only.
    So, we return 1.
Input 2:
    A = 2
Output 2:
    2
Explanation 2:
    If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
    {(1-2), (3-4)} and {(1-4), (2-3)}.
    So, we return 2.
"""


# Think in terms of DP.
# Can we relate answer for N with smaller answers.
# If we draw a chord between any two points, can you observe current set of points getting broken into two
# smaller sets S_1 and S_2? Can a chord be drawn between two points where each point belong to different set?
# If we draw a chord from a point in S_1 to a point in S_2, it will surely intersect the chord we’ve just drawn.
# So, we can arrive at a recurrence that Ways(n) = sum[i = 0 to n-1] { Ways(i)*Ways(n-i-1) }.
# Here we iterate over i, assuming that size of one of the sets is i and size of other set automatically
# is (n-i-1) since we’ve already used a pair of points and i pair of points in one set.

class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        from math import factorial
        ans = factorial(2 * A) // factorial(A + 1)
        ans = ans // factorial(A)
        ans = ans % (10 ** 9 + 7)
        return ans
