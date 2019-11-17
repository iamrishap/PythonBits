"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Given s = "Hello World",
return 5 as length("World") = 5.
Please make sure you try to solve this problem without using library functions.
Make sure you only traverse the string once.
"""

# How can you detect the end of the string?
# How can you detect where the word begins?
# What if you maintained the length of the current word?
# You reset the length of the word when the next word begins (When does a new word begin?)
# Return the last length you have.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        counter = 0
        if A == "":
            return 0
        else:
            for c in A[::-1]:
                if c == " ":
                    if counter != 0:
                        return counter
                else:
                    counter += 1
            return counter
