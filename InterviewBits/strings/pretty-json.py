"""
Given a string A representing json object. Return an array of string denoting json object with proper indentation.
Rules for proper indentation:
Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:
[] and {} are only acceptable braces in this case.
Assume for this problem that space characters can be done away with.
Input Format
The only argument given is the integer array A.
Output Format
Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character.
For Example
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }
Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
"""


# This is more of a parsing problem.
# Make sure you take a lot of time thinking about the corner cases and structure of the code before you start coding.
# Fixing corner cases on the fly can make your code really ugly.
# Note the following:
# 1) ‘{‘, ‘[’ have the same effect on the printing
# 2) ‘}’, ‘]’ have the same effect as well
# 3) ‘:’ and ‘,’ are the only other 2 characters that matter.
# Think about the behavior when you encounter the following characters.
# Also think about the behavior based on the following character.

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        indent = 0
        res = []
        line = ''
        for x in A:
            if x in '{[':
                if line:
                    res.append(line)
                res.append('\t' * indent + x)
                line = ''
                indent += 1
            elif x in ']}':
                if line:
                    res.append(line)
                indent -= 1
                line = '\t' * indent + x  # Might be followed by ','
            else:
                if not line:
                    line = '\t' * indent
                line += x
                if x == ",":
                    res.append(line)
                    line = ''
        if line:
            res.append(line)
        return res


s = Solution()
print(s.prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'))
