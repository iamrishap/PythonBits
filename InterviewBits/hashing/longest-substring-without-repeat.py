"""
Given a string,
find the length of the longest substring without repeating characters.
Example:
The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
"""


# Think in terms of two pointers.
# If you encounter a repeating character, you won’t be able to include the new character till you exclude out the
# previous occurrence of the character. Which means your window needs to shrink till your start character is pointing
# to the position next to previous occurrence of the character.
# All you need to do is use two pointers to keep a window with no repetitions of characters. Keep moving the right
# pointer and if you encounter any repeating character start moving left pointer untill no character is repeated.
# Also, note that the size of character set is small ( 128 at max ), so tracking the count of characters in the
# current set is fairly easy using hashing / array buckets.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        i = j = result = 0
        sz = len(A)
        storage = set()
        while i < sz and j < sz:
            if A[j] in storage:
                storage.remove(A[i])
                i += 1
            else:
                storage.add(A[j])
                j += 1
                result = max(result, j - i)
        return result
