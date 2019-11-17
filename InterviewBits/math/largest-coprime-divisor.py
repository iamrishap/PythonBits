"""
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,
A = 30
B = 12
We return
X = 5
"""


# We know A is the greatest number dividing A. So if A and B are coprime, we can return the value of X to be A.
# Else, we can try to remove the common factors of A and B from A.
# We can try to remove the common factors of A and B from A by finding the greatest common divisor
# (gcd) of A and B and dividing A with that gcd.
# Mathematically, A = A / gcd(A, B) —— STEP1
# Now, we repeat STEP1 till we get gcd(A, B) = 1.
# Atlast, we return X = A

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while True:
            A1 = A
            B1 = B
            # Find gcd
            while B1 > 0:
                A1, B1 = B1, A1 % B1
            if A1 == 1:
                return A
            A = A // A1
        return A
