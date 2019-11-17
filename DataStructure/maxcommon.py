a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8, 10]

def maxcommon(a, b):
    aset = set(a)
    bset = set(b)
    print(aset & bset)

maxcommon(a, b)
