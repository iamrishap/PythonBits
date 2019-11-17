"""
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all
the bulbs to the right of current bulb.
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.
Note : 0 represents the bulb is off and 1 represents the bulb is on.
Input Format:
The first and the only argument contains an integer array A, of size N.
Output Format:
Return an integer representing the minimum number of switches required.
Constraints:
1 <= N <= 5e5
0 <= A[i] <= 1
Example:
Input 1:
    A = [1]
Output 1:
    0
Explanation 1:
    There is no need to turn any switches as all the bulbs are already on.
Input 2:
    A = [0 1 0 1]
Output 2:
    4
Explanation 2:
    press switch 0 : [1 0 1 0]
    press switch 1 : [1 1 0 1]
    press switch 2 : [1 1 1 0]
    press switch 3 : [1 1 1 1]
"""


# The order in which you press the switch does not affect the final state.
# Example:
# Input : [0 1 0 1]
# Case 1:
# 	Press switch 0 : [1 0 1 0]
# 	Press switch 1 : [1 1 0 1]
# Case 2:
# 	Press switch 1 : [0 0 1 0]
# 	Press switch 0 : [1 1 0 1]
# Therefore we can choose a particular order. To make things easier lets go from left to right.
# At the current position if the bulb is on we move to the right, else we switch it on.
# This works because changing any switch to the right of it will not affect it anymore.

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        def flip(i):
            return 0 if i else 1

        off = 0
        num = 0
        for i in range(len(A)):
            if A[i] == off:
                num += 1
                off = flip(off)
        return num
