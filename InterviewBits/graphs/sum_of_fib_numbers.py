"""
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
"""


class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        from itertools import combinations
        if A == 0:
            return 0
        fact_list = [1, 1]
        last = fact_list[-1] + fact_list[-2]
        while last <= A:
            fact_list.append(last)
            last = fact_list[-1] + fact_list[-2]
        for i in range(len(fact_list[::-1])):  # Reversing the list to try bigger number first
            if len([comb for comb in combinations(fact_list, i + 1) if sum(comb) == A]) > 0:
                return i + 1

    def fibsum_editorial(self, A):
        # Uses Greedy Approach
        """
        Zeckendorf's theorem states that every positive integer can be represented uniquely as the sum
        of one or more distinct Fibonacci numbers in such a way that the sum does not include any two
        consecutive Fibonacci numbers.
        """
        F = [1, 1]
        while F[-1] < A:
            F.append(F[-1] + F[-2])
        rem = A
        count = 0
        while rem > 0:
            if F[-1] > rem:
                F.pop()
            else:
                rem -= F[-1]
                count += 1
        return count


s = Solution()
print(s.fibsum(7))
