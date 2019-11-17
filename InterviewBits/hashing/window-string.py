"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.
Example :
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"
 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
"""

# Essentially you have a start and end pointer starting from the beginning of the string. You keep moving the end
# pointer and including more characters till you have all the characters of T included. At this point, you start
# moving start pointer and popping out characters till the point that you still have all the characters of T included.
# Update your answer and keep repeating the process.

from collections import deque


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if not A or not B:
            return ''
        required_chars = {}
        for b in B:
            if b not in required_chars:
                required_chars[b] = deque()
            required_chars[b].append(-1)
        n_needed = len(B)

        best = None
        cur_min = None
        for idx, a in enumerate(A):
            if a in required_chars:
                old_idx = required_chars[a].popleft()
                required_chars[a].append(idx)
                if n_needed != 0 and old_idx == -1:
                    n_needed -= 1
                if n_needed == 0 and (cur_min is None or old_idx == cur_min):
                    cur_min = min([a[0] for a in required_chars.values()])
                    if best is None or best[1] - best[0] > idx - cur_min:
                        best = [cur_min, idx]
        if best is None:
            return ''
        return A[best[0]:best[1] + 1]
