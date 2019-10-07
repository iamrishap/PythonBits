matrix = [
    [1, 2,  3,   4],
    [5, 6,  7,   8],
    [9, 10, 11, 12]
]

def rotate(matrix, clock=True):
    if clock:
        print(list(map(list, zip(*matrix))))
    else:
        print(list(map(list, zip(*matrix)))[::-1])

rotate(matrix, True)