"""
Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.
Look at the example for more details.
Example
A = 5
Return: [1 2 Fizz 4 Buzz]
"""


# While Iterating from 1 to N, you need to check the following conditions in sequence:
#
# Check whether the number is divisible by 3 and 5, if that is the case, print FizzBuzz.
# Check whether the number is divisible by 3, in that case, print Fizz.
# Next, check whether the number is divisible by 5, in that case print Buzz.
# Otherwise, print the number.
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ans = [i for i in range(1, A + 1)]
        for i in range(2, A, 3):
            ans[i] = "Fizz"
        for i in range(4, A, 5):
            ans[i] = "Buzz"
        for i in range(14, A, 15):
            ans[i] = "FizzBuzz"
        return ans

    def fizzBuzz_iterative(self, A):
        sol = []
        for i in range(1, A + 1):
            if i % 3 == 0 and i % 5 == 0:
                sol.append("FizzBuzz")
            elif i % 3 == 0:
                sol.append("Fizz")
            elif i % 5 == 0:
                sol.append("Buzz")
            else:
                sol.append(i)
        return sol
