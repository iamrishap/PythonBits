"""
Largest Number
Asked in: Amazon, Goldman Sachs, Microsoft

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9, 91], the largest formed number is 919534330.

Note: The result may be very large, so you need to return a string instead of an integer.

NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function.
Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
"""
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber_old(self, A):
        # Fails in cases like: 298 29
        # Various padding value were used like 0, 9, last digit, last digit - 1 but they all have issues
        sol_array, max_len, solution = [], 0, ''
        # Finding the max length value
        for val in A:
            if len(str(val)) > max_len:
                max_len = len(str(val))
        # Converting each value to length `max_len` and storing the number of digits appended
        # We are repeating a value less than the last digit for padding, for proper comparison reasons
        for val in A:
            num = val
            if len(str(val)) < max_len:
                num = int(str(val) + str(val % 10) * (max_len - len(str(val))))
            sol_array.append((num, max_len - len(str(val))))

        sol_array = sorted(sol_array, key=lambda x: (-x[0], -x[1]))
        # Generating the solution string by removing the appended digits
        for val in sol_array:
            solution += ' ' + str(val[0]) if val[1] == 0 else ' ' + str(val[0])[:-val[1]]
        return solution

    def largestNumber(self, A):
        import functools
        A = map(str, A)
        res = ''.join(sorted(A, key=functools.cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1), reverse=True))
        return int(res) if res else '0'

s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([0, 0, 0, 0, 0]))
print(s.largestNumber([12, 121]))
print(s.largestNumber([9, 99, 999, 9999, 9998]))
print(s.largestNumber([782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357,
                       261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298,
                       470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905]))

