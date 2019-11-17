"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
Input Format:
The first and the only argument is a string A.
Output Format:
Return an integer, representing the number of ways to decode the string.
Constraints:
1 <= length(A) <= 1e5
Example :
Input 1:
    A = "8"
Output 1:
    1
Explanation 1:
    Given encoded message "8", it could be decoded as only "H" (8).
    The number of ways decoding "8" is 1.
Input 2:
    A = "12"
Output 2:
    2
Explanation 2:
    Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
    The number of ways decoding "12" is 2.
"""


# So, when looking at the start of the string, we can either form a one digit code, and then look at the ways of
# forming the rest of the string of length L - 1, or we can form 2 digit code if its valid and add up the ways
# of decoding rest of the string of length L - 2.


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if len(A) == 0:
            return 0

        # No decoding starting with 0 will be a valid decoding.
        if int(A[0]) == 0:
            return 0

        n = len(A)

        # Mark everything as zero initially
        result = [0 for _ in range(0, n + 1)]  # Notice how it is initialized to size n+1 not n

        # Now that we know that the string does not begin with zero,
        # the minimum number of decodings for a length 2 string will be 1.
        # So mark both as 1.
        result[0] = result[1] = 1

        for i in range(1, n):

            # At every step, we can either decode 1 or 2 characters. Fish them out.
            v1 = int(A[i:i + 1])
            v2 = int(A[i - 1:i + 1])

            # A number starting with 0, won't be a valid single number decoding.
            # It can only fit with either 10 or 20 (depends on previous number)
            if 0 < v1 <= 9:
                # If we get a valid single number decoding, the number of decodings will
                # same as previous. Because a single valid decoding won't add to your count.
                result[i + 1] = result[i]

            if 10 <= v2 <= 26:
                # Check if a double number decoding is valid.
                # If it is valid, we need to add everything before this two digit number to the current number.
                result[i + 1] = result[i + 1] + result[i - 1]

            # At any state, if we are not able to modify something, it is invalid.
            if result[i + 1] == 0:
                return 0

        answer = result[n]
        return answer


s = Solution()
print(s.numDecodings("121"))
