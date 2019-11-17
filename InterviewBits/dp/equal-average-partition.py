"""
Given an array with non negative numbers, divide the array into two parts such that the average of both the parts is equal.
Return both parts (If exist).
If there is no solution. return an empty list.
Example:
Input:
[1 7 15 29 11 9]
Output:
[9 15] [1 7 11 29]
The average of part is (15+9)/2 = 12,
average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
 NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A and B which
 follow the following condition :
numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller than B
( https://en.wikipedia.org/wiki/Lexicographical_order )
NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie,
return the one where A is lexicographically smallest. NOTE 3: Array will contain only non negative numbers.
"""

# Lets try to simplify the problem.
# Lets assume the two sets are set1 and set2.
# Assume sum of set1 = Sum_of_Set1, with size = size_of_set1.
# Assume sum of set2 = Sum_of_Set2, with size = size_of_set2
#  SUM_of_Set1 / size_of_set1 = SUM_of_Set2 / size_of_set2
#  SUM_of_Set1 = SUM_of_Set2 * (size_of_set1 / size_of_set2)
#     total_sum = Sum_of_Set1 + Sum_of_Set2
#     AND size_of_set2 = total_size - size_of_set1
#   Sum_of_Set1 = (total_sum - Sum_of_Set1) * (size_of_set1 / (total_size - size_of_set1))
#   OR on simplifying,
#   total_sum / Sum_of_Set1 - 1 = (total_size - size_of_set1) / size_of_set1
#   total_sum / Sum_of_Set1 = total_size / size_of_set1
#   Sum_of_Set1 / size_of_set1 = total_sum / total_size
# Note that you need the solution with minimum size_of_set1 if multiple solutions exist.
# So, just iterate on size_of_set1.
# Based on size_of_set1, you can determine the value of Sum_of_Set1.
# Now, the problem reduces to
#
# Can I select size_of_set1 values from the array whose sum is Sum_of_Set1 ?
# In previous hint, we explored how we can break down the given problem into a much simpler problem
#
# Can I select current_size values from the array whose sum is current_sum ?
# Lets define our function as
# isPossible(ind, current_sum, current_size) which returns true if it is possible to use elements with index >= ind
# to construct a set of size current_size whose sum is current_sum.
# isPossible(ind, current_sum, current_size :
#                            |
#                            |
#                            |  isPossible(ind + 1, current_sum, current_size)  [ Do not include current element ]
#     Or(|) Logical operator |
#                            |
#                            |
#                            |
#                            |  isPossible(ind + 1, current_sum - value_at(ind), current_size - 1)
#                            |
# Can you memoize values to reduce the time complexity of the above recursive function ?

from functools import wraps
import fractions


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    @memo
    def knapsack(self, i, num, tot):
        # Find num items in A that add up to tot
        if i > len(self.A) - 1 or num <= 0 or tot <= 0:
            return None
        elif num == 1 and self.A[i] == tot:
            return [self.A[i]]
        else:
            include = self.knapsack(i + 1, num - 1, tot - self.A[i])
            exclude = self.knapsack(i + 1, num, tot)

            if include:
                return [self.A[i]] + include
            elif exclude:
                return exclude

    def avgset(self, A):
        tot = sum(A)
        n = len(A)

        gcd = fractions.gcd(tot, n)

        num = n // gcd
        self.A = sorted(A)

        for i in range(num, n // 2 + 1, num):
            k = self.knapsack(0, i, tot * i // n)
            if k is not None:
                temp = k[:]
                return [k, [i for i in self.A if not i in temp or temp.remove(i)]]
        return []
