"""
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
Chech whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.
Note: A will be always a valid expression.
Input Format
The only argument given is string A.
Output Format
Return 1 if string has redundant braces, else return 0.
For Example
Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.
Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.
"""


# If we somehow pick out sub-expressions surrounded by ( and ),
# then if we are left with () as a part of the string, we know we have redundant braces.
# Lets take an example:
# (a+(a+b))
# We keep pushing elements onto the stack till we encounter ')'.
# When we do encounter ')', we start popping elements till we find a matching '('.
# If the number of elements popped do not correspond to '()', we are fine and we can move forward.
# Otherwise, voila! Matching braces have been found.
# Some Extra Hints:
# Try to run your code on test cases like (a*(a))  and (a) ??

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] in '(+-/*':
                stack.append(A[i])
            elif A[i] == ')':
                if stack.pop() == '(':
                    return 1
                stack.pop()
        return 0
