from collections import Counter
def rotator(A):
    '''
    >>> A = [[1, 2, 3], \
        [4, 5, 6],\
        [7, 8, 9]]
    >>> rotator(A)
    [(7, 4, 1), (8, 5, 2), (9, 6, 3)]
    '''
    print([a[::-1] for a in zip(*A)])
    # print(list(map(list, zip(*A)))[::-1])


def duplicates(A):
    '''
    >>> duplicates([1,2,3,4,5,6,7,8,9,1,2])
    [1, 2]
    '''
    print([item for item, count in Counter(A).items() if count > 1])

def spiral_matrix(A):
    '''
    >>> A = [[1, 2, 3], \
        [4, 5, 6],\
        [7, 8, 9]]
    >>> spiral_matrix(A)
    '''
    # TODO : Write other methods also. Use itertools.chain
    while A:
        print(A[0])
        A = list(reversed(list(zip(*A[1:]))))

def repeat_and_missing(A):
    '''
    >> > repeat_and_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
    1 10
    '''
    for i in range(len(A)):
        if A[i] >= 0:
            if A[A[i]] >= 0:
                A[A[i]] = -1
            else:
                print(A[i])
    # for i in range(len(A)):
    #     if A[i] > 0:
    #         print(A[i])

def matrix_zero(A=None):
    import pprint

    m = [[1, 0, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1]]

    N = len(m)

    ### pass 1

    # 1 rst line/column
    c = 1
    for i in range(N):
        c &= m[i][0]

    l = 1
    for i in range(1, N):
        l &= m[0][i]

    # other line/cols
    # use line1, col1 to keep only those with 1
    for i in range(1, N):
        for j in range(1, N):
            if m[i][j] == 0:
                m[0][j] = 0
                m[i][0] = 0
            else:
                m[i][j] = 0

    ### pass 2

    # if line1 and col1 are ones: it is 1
    for i in range(1, N):
        for j in range(1, N):
            if m[i][0] & m[0][j]:
                m[i][j] = 1

    # 1rst row and col: reset if 0
    if l == 0:
        for i in range(N):
            m[i][0] = 0

    if c == 0:
        for j in range(1, N):
            m[0][j] = 0

    pprint.pprint(m)

matrix_zero()