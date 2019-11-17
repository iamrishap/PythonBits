"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach’s conjecture
Example:
Input : 4
Output: 2 + 2 = 4
If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

# This problem’s solution is straight forward.
# Generate prime numbers less than N, and hash them in a list.
# Then iterate on the whole list, and for every prime P, check if N-P is also prime.
# If you find such a pair, you are done :)
# Coming to the problem of generating prime numbers quickly, we already have a problem SIEVE where we did it.
# However, re-iterating, there are multiple ways of doing it. Probably the easiest way is Sieve of Erastothenes.

import math


class Solution:
    def primesum(self, n: int) -> 'List[int]':
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        # Sieve of Erastothenes for constructing map of primes
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False

        for i in range(2, n):
            if is_prime[i] and is_prime[n - i]:  # Found a prime pair
                return [i, n - i]
        return []


s = Solution()
print(s.primesum(5))
