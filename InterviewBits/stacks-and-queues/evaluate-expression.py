"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Input Format
The only argument given is character array A.
Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.
For Example
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
"""


# This is pretty much a simulation problem.
# Think stack.
# When you encounter an operator is when you need the top 2 numbers on the stack,
# perform the operation on them and put them on the stack.

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        group = {'+': 1, '-': 2, '*': 3, '/': 4}

        def sumi(a, b):
            return a + b

        def sub(a, b):
            return b - a

        def mul(a, b):
            return int(a * b)

        def div(a, b):
            return int(b / a)

        for i in range(len(A)):
            if A[i] not in group:
                stack.append(A[i])
            else:
                val = group[A[i]]
                a = int(stack.pop())
                b = int(stack.pop())
                if val == 1:
                    stack.append(sumi(a, b))
                elif val == 2:
                    stack.append(sub(a, b))
                elif val == 3:
                    stack.append(mul(a, b))
                elif val == 4:
                    stack.append(div(a, b))
        return stack[0]
