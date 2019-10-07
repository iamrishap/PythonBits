"""
Given three prime number(p1, p2, p3) and an integer k. Find the first(smallest) k integers which
have only p1, p2, p3 or a combination of them as their prime factors.

Example:

Input :
Prime numbers : [2,3,5]
k : 5

If primes are given as p1=2, p2=3 and p3=5 and k is given as 5, then the sequence of first 5 integers will be:

Output:
{2,3,4,5,6}

Explanation :
4 = p1 * p1 ( 2 * 2 )
6 = p1 * p2 ( 2 * 3 )

Note: The sequence should be sorted in ascending order
"""


class Solution:
    def solve(self, A, B, C, D):
        """
        Failed to give the right answer. It doesn't know how many combinations to use to get to the answer.
        If there is a very small prime number, it is better to reuse it repeatedly instead of choosing other primes.
        """
        seq = set()
        i = 1
        from itertools import combinations_with_replacement
        from functools import reduce
        import operator
        reduce(operator.mul, (3, 4, 5), 1)
        while i < 9:  # len(seq) < D and
            seq.update([reduce(operator.mul, comb, 1) for comb in combinations_with_replacement([A, B, C], i)])
            i += 1
        return sorted(list(seq))[: D]

    def solve_editorial(self, A, B, C, D):
        prime1 = A
        prime2 = B
        prime3 = C
        count = 0
        ans = []
        i, j, k = 0, 0, 0
        while count != D:
            temp = min(prime1, prime2, prime3)
            ans.append(temp)
            count += 1
            if temp == prime1:
                prime1 = A * ans[i]
                i += 1
            if temp == prime2:
                prime2 = B * ans[j]
                j += 1
            if temp == prime3:
                prime3 = C * ans[k]
                k += 1
        return ans


s = Solution()
# print(s.solve(2, 3, 4, 5))
# print(s.solve(2, 5, 11, 3))
# print(s.solve(3, 11, 7, 50))
print(s.solve_editorial(3, 11, 7, 50))
