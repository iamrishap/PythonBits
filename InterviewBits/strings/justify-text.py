"""
Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
Your program should return a list of strings, where each string represents a single line.
Example:
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""


# This problem is more of simulation. Take care of some of corner cases like space distribution in different lines.
# Corner Cases:
# 1) A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
# 2) Have you noticed that the last line is an exception in terms of spaces?
# This is more of a simulation problem. The more elegant your code, the less chances of it being bug prone,
# and more marks in the interview.
# Give a lot of thought to the structure of the code before you start coding.

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def splitWords(self, words, curr, L):
        if len(words) == 1:
            return words[0] + " " * (L - curr)
        to_all = (L - curr) // (len(words) - 1)
        additional = (L - curr) % (len(words) - 1)
        res = words.pop(0)

        for word in words:
            res += " " * (to_all + 1)
            if additional > 0:
                res += " "
                additional -= 1
            res += word
        return res

    def fullJustify(self, A, B):
        result = []
        curr = 0
        tmp = []
        for word in A:
            if not word:
                continue
            if curr + len(word) <= B:
                curr += len(word) + 1
                tmp.append(word)
            else:
                result.append(self.splitWords(tmp, curr - 1, B))
                tmp = [word]
                curr = len(word) + 1
        if curr:
            result.append(' '.join(tmp) + ' ' * (B - curr + 1))
        return result


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

# TODO: Didn't understood it exactly. Revisit.
