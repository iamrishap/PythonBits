import sys
def canBeBST(preorder):
    if not preorder:
        return "NO"
    stack = []
    root = -sys.maxsize
    for item in preorder:
        if item < root: # root will change only once, when set from stack.pop()
            return "NO"
        while len(stack) > 0 and stack[-1] < item: # First decreasing, then increasing sequence
            root = stack.pop()
        stack.append(item)
    return "YES"

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        _, preorder = input(), list(map(int,input().split()))
        print(canBeBST(preorder))