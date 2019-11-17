"""
Given N and M find all stepping numbers in range N to M

The stepping number:
A number is called as a stepping number if the adjacent digits have a difference of 1.
e.g 123 is stepping number, but 358 is not a stepping number

Example:
N = 10, M = 20
all stepping numbers are 10 , 12
Return the numbers in sorted order.
"""

import heapq


class Solution:
    def stepnum(self, A, B):

        ans = []
        # Starts with these numbers and adds one/two numbers for each
        # by either adding one more or reducing once from the end
        final = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        heapq.heapify(final)
        group = set()  # To store which group of number have been processed
        for i in range(11):
            group.add(i)
        while 1:
            val = heapq.heappop(final)
            if val > B:
                break
            if val >= A:
                ans.append(val)

            if str(val)[-1] == '0':
                if val * 10 + 1 not in group:
                    heapq.heappush(final, val * 10 + 1)
                    group.add(val * 10 + 1)
            elif str(val)[-1] == '9':
                if val * 10 - 1 not in group:
                    heapq.heappush(final, val * 10 - 1 + int(str(val)[-1]))
                    group.add(val * 10 - 1)
            else:
                if val * 10 + 1 not in group:
                    heapq.heappush(final, val * 10 + 1 + int(str(val)[-1]))
                    group.add(val * 10 + 1)
                if val * 10 - 1 not in group:
                    heapq.heappush(final, val * 10 - 1 + int(str(val)[-1]))
                    group.add(val * 10 - 1)
        return ans


s = Solution()
# print(s.stepnum(200, 300))
print(s.stepnum(10, 30))
