"""
Given a set of digits (A) in sorted order, find how many numbers of
length B are possible whose value is less than number C.
 NOTE: All numbers can only have digits from the given set.
Examples:
    Input:
    0 1 5
    1
    2
    Output:
    2 (0 and 1 are possible)
    Input:
    0 1 2 5
    2
    21
    Output:
    5 (10, 11, 12, 15, 20 are possible)
Constraints:
    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
"""


# Find solution of each cases separately.
# Case 1 : When B is greater than length of C
# Case 2: When B is smaller than length of C
# Case 3: When B is equal to length of C.
# For case 3:
# Let First(i) denote number formed by taking first i digits of C
# Then try to find a relation between solution of (A, i, first(i)) and (A, i - 1, first(i - 1)) for i = 1 to i <= B
# Let us try to solve for all the possible cases.
# Let d be size of A, B is the length, C is the max number
# Case 1: If B is greater than length of C or d is 0 then no such number is possible.
# Case 2: If B is smaller than length of C then ALL the possible combination of digits of length B are valid.
# Generate all such B digit numbers.
# For the first position we can’t have 0 and for the rest of (B - 1) position we can have all d possible digits.
# Hence, Answer = d*B if A contains 0 else (d-1) * ( d )(B-1)
# Case 3: If B is equal to length of C
# Construct digit array of C ( call it as digit[]).
# Let First(i) be a number formed by taking first i digits of it.
# Let lower[i] denote number of elements in A which are smaller than i.
# It can be easily computed by idea similar to prefix sum.
# For example:
# First(2) of 423 is 42.
# If  A =  [ 0, 2] then lower[0] = 0, lower[1]  = 1,  lower[2] = 1, lower[3] = 2
# Generate B digit numbers by dynamic programming. Let say dp[i] denotes the total numbers of length
# i which are less than first i digits of C.


class Solution:
    def count(self, A, B, b, i):
        if i >= len(b) or B == 0:
            return 1
        c_max = int(b[i])
        rt = 0
        for x in A:
            if i == 0 and x == 0 and B != 1:
                continue
            if x > c_max:
                continue
            if x == c_max:
                if i >= len(b) - 1:
                    continue
                rt = rt + self.count(A, B - 1, b, i + 1)
            else:
                rt = rt + len(A) ** (B - 1)
        return rt

    def solve(self, A, B, C):
        c = str(C)
        if len(c) < B:
            return 0

        ind = 0
        if len(c) == B:
            return self.count(A, B, c, 0)
        rt = 0
        for x in A:
            if x == 0 and B != 1:
                continue
            if x == 0 and x < C:
                rt += 1
            else:
                rt = rt + len(A) ** (B - 1)
        return rt

# TODO: Didn't spend time understanding it. Revisit.
