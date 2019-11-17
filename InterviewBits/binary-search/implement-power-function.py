"""
Implement pow(x, n) % d.
In other words, given x, n and d,
find (xn % d)
Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.
Input : x = 2, n = 3, d = 3
Output : 2
2^3 % 3 = 8 % 3 = 2.
"""


# You need to come up with a solution better than O(n).
# Think recursively. You can think of an example like 3^8. How many multiplication do you really need to evaluate 3^8?
# There are two major things to note here:
# 1) Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.
# 2) Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).
# If n is even, note the following:
# x ^ n = (x * x) ^ n/2
# Can you use the above observation to come up with a solution better than O(n)?

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 1 % d
        ans = 1
        base = x
        base = base % d

        while n > 0:
            # We need (base ** n) % p.
            # Now there are 2 cases.
            # 1) n is even. Then we can make base = base^2 and n = n / 2.
            # 2) n is odd. So we need base * base^(n-1)
            if n % 2 == 1:
                ans = (ans * base) % d
                n -= 1
            else:
                n = n >> 1
                base = (base * base) % d
        # if ans < 0:
        #     ans = (ans + d) % d
        return ans

# TODO: Revisit. Easy question. Could be asked.
