"""
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how
much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the
constraints that any painter will only paint contiguous sections of board.
2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003
Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board
Output:
     return minimum time to paint all boards % 10000003
Example
Input :
  K : 2
  T : 5
  L : [1, 10]
Output : 50
"""


# If you have already solved the problem corresponding to hint1, you are already halfway there.
# You can do a binary search for the answer :
#   start = 0, end = max_time_possible
#   mid = (start + end) / 2
#   if isPossible(mid):
#   	end = mid - 1
#   else
# 	start = mid + 1
# Now, lets look into how isPossible would be implemented.
# Keep assigning boards to painter greedily till the time taken < mid. If you run out of painters, isPossible = false.
# else isPossible = true.

def is_poss(sumi, l, k):
    m = 0
    cur_sum = 0
    for i in range(len(l)):
        if l[i] > sumi:
            return False
        if l[i] + cur_sum <= sumi:
            cur_sum += l[i]
        else:
            m += 1
            cur_sum = l[i]

    if m == 0 or m >= k:
        return False

    return True


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        start = 0
        end = sum(C)

        while start < end:

            mid = (start + end) // 2
            if is_poss(mid, C, A):
                end = mid
            else:
                start = mid + 1

        return (start * B) % 10000003


# TODO: Left due to complexity. Revisit.
