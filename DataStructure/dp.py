import doctest
import sys
doctest.testmod()

def lcs(strone, strtwo):
    '''
    >>> lcs('rohsaahp', 'rishap')
    rhap
    '''
    if not strone or not strtwo:
        return ""
    startone, leftone, starttwo, lefttwo = strone[0], strone[1:], strtwo[0], strtwo[1:]
    if startone == starttwo:
        return startone + lcs(leftone, lefttwo)
    else:
        return max(lcs(strone, lefttwo), lcs(leftone, strtwo), key=len)


def lcs_dp(strone, strtwo):
    '''
    >>> lcs_dp('it con rieongs.adfe', 'this is the second string sample.')
    it con ringsae
    '''
    x, y = len(strone), len(strtwo)
    table = [[0 for i in range(y + 1)] for j in range(x + 1)]
    for i in range(x):
        for j in range(y):
            if strone[i] == strtwo[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

    result = ''
    i, j = x, y
    while i != 0 and j != 0:
        if table[i][j] == table[i - 1][j]:
            i -= 1
        elif table[i][y] == table[i][j - 1]:
            j -= 1
        else:
            result = strone[i - 1] + result
            i -= 1
            j -= 1
    return result


def max_value_contagious(vals):
    '''
    >>> a = [3, -1, 7, -10, 5, 3, 0, 8]
    >>> max_value_contagious(a)
    16
    '''
    if not filter(lambda x: x >= 0, vals):
        return 0
    max_yet = max_now = 0
    for val in vals:
        if val + max_now > 0:
            max_now += val
        else:
            max_now = 0
        if max_now > max_yet:
            max_yet = max_now
    return max_yet


def max_value_alternate(vals):
    '''
    >>> a = [3, 1, 7, 10, 5, 3, 0, 8]
    >>> max_value_alternate(a)
    24
    '''
    # maximum = 0
    M = []
    M.append(vals[0])
    base_two = vals[0] if vals[0] > vals[1] else vals[1]
    M.append(base_two)
    for i, val in enumerate(vals[2:]):
        M.append(max(M[i + 1], M[
            i] + val))  # as i starts with value less than normal. Used i+1 instead of i-1 and i instead of i-2
    return M[len(vals) - 1]


def subset_sum(vals, sum):
    '''
    >>> subset_sum([1,3,5,10], 17)
    0
    >>> subset_sum([3, 2, 4, 19, 3, 7, 13, 10, 6, 11], 17)
    1
    '''
    if not vals:
        return 0 if sum != 0 else 1
    l = len(vals)
    m = [[0 for i in range(sum + 1)] for j in range(l + 1)]
    for i in range(l + 1):
        m[i][0] = 1
    for i in range(1, l + 1):
        for j in range(1, sum + 1):
            m[i][j] = m[i - 1][j]
            if j >= vals[i - 1]:
                m[i][j] = m[i][j] or m[i - 1][j - vals[i - 1]]
    return m[l][sum]


def half_sum_subset(vals):
    '''
    >>> half_sum_subset([3, 2, 4, 19, 3, 7, 13, 10, 6, 11])
    1
    >>> half_sum_subset([3, 5, 2])
    1
    '''
    if not vals:
        return 0
    K = sum(vals)
    possible = [0] * (K + 1)
    vals.sort()
    possible[0] = possible[vals[0]] = 1
    R = vals[0]
    for i in range(len(vals)):
        for j in range(R, -1, -1):
            if possible[j] and j + vals[i] <= K // 2:
                possible[j + vals[i]] = 1
            R = min(K // 2, R + vals[i])
    return possible[K // 2]


def editDistance(A, B):
    '''
    >>> editDistance("HelJoworld", "HalloWorlduu")
    5
    '''
    m = len(A) + 1
    n = len(B) + 1
    table = {}
    for i in range(m):  table[i, 0] = i
    for j in range(n):  table[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if A[i - 1] == B[i - 1] else 1
            table[i, j] = min(table[i, j - 1] + 1, table[i - 1, j] + 1, table[i - 1, j - 1] + cost)
    return table[i, j]


def floydWarshall(graph):
    '''
    >>> graph = {'A': {'A': 0, 'B': 6, 'C': INF, 'D': 6, 'E': 7}, \
             'B': {'A': INF, 'B': 0, 'C': 5, 'D': INF, 'E': INF}, \
             'C': {'A': INF, 'B': INF, 'C': 0, 'D': 9, 'E': 3}, \
             'D': {'A': INF, 'B': INF, 'C': 9, 'D': 0, 'E': 7}, \
             'E': {'A': INF, 'B': 4, 'C': INF, 'D': INF, 'E': 0} \
             }
    >>> INF = sys.maxsize
    >>> floydWarshall(graph)
    {'A': {'A': 0, 'B': 6, 'C': 11, 'D': 6, 'E': 7}, 'B': {'A': 2147483647, 'B': 0, 'C': 5, 'D': 14, 'E': 8}, 'C': {'A': 2147483647, 'B': 7, 'C': 0, 'D': 9, 'E': 3}, 'D': {'A': 2147483647, 'B': 11, 'C': 9, 'D': 0, 'E': 7}, 'E': {'A': 2147483647, 'B': 4, 'C': 9, 'D': 18, 'E': 0}}
    '''
    nodes = graph.keys()
    distance = {}
    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


def coin_game():
    coins = [1, 2, 3, 4, 5]
    n = len(coins)
    # each time it is our turn, take the max of the two available moves (but the minimum of
    # the opponent's two  potential moves)
    v = []
    for i in range(n):
        v.append([0] * n)
    for i in range(n):
        for j in range(n):
            if i == j:
                v[i][j] = coins[i]
            elif j == i + 1:
                v[i][i] = max(coins[i], coins[j])
            # only valid  if i < j
            if (i + 2) <= j:
                take_start = v[i + 2][j]
            else:
                take_start = 0
            if (i + 1) <= (j - 1):
                take_end = v[i + 1][i - 1]
            else:
                take_start = 0
    print(v)


def longest_palin_subseq(str):
    '''
    >>> longest_palin_subseq("GEEKS FOR GEEKS")
    7
    '''
    n = len(str)
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])
    return L[0][n - 1]


def palindromes(text):
    '''
    >>> palindromes('abccba')
    (0, ['cc', 'bccb', 'abccba'])
    '''
    text = text.lower()
    results = []
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    return text.index(max(results, key=len)), results

def longest_palin_substr_dp(text):
    pass


def longest_palin_substr(string):
    '''
    >>> longest_palin_substr("forgeeksskeegford")
    10
    '''
    maxLength = 1
    start = 0
    length = len(string)
    low = 0
    high = 0
    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
    # print(string[start:start + maxLength])
    return maxLength

def biggest_square(N):
    '''
    >>> biggest_square([[0, 1, 1, 0, 1 ], [1, 1, 0, 1, 0 ], [0, 1, 1, 1, 0 ], [1, 1, 1, 1, 0 ], [1, 1, 1, 1, 1 ], [0, 0, 0, 0, 0 ]])
    3
    '''
    rows, cols = len(N), len(N[0]) if N else 0
    if not rows or not cols:
        return 0
    M = [[0 for _ in range(cols)] for __ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if N[i][j] == 1:
                if i == 0 or j == 0:
                   M[i][j] = N[i][j]
                else:
                    M[i][j] = min(M[i-1][j-1], M[i][j-1], M[i-1][j]) + 1
    return max(max(r) for r in M)


def biggest_rectangle_area(M):
    '''
    >>> a = [[2, 3, 3, 5, 2]]
    >>> biggest_rectangle_area(a)
    10
    >>> a = [[1,6,2,5,4,5,1,6]]
    >>> biggest_rectangle_area(a)
    12
    >>> a=[ \
        [1, 1, 0, 0, 1, 0], \
        [0, 1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1, 0], \
        [0, 0, 1, 1, 0, 0]  \
       ]
    >>> biggest_rectangle_area(a)
    8
    '''
    def generate_histograms(M):
        rows, cols = len(M), len(M[0]) if M else 0
        if not rows:
            return None
        for i in range(1, rows):
            for j in range(cols):
                if M[i][j] == 1:
                    M[i][j] = M[i-1][j] + 1
        return M

    def get_max_area(hg):
        stack = []
        i = 0
        maximum = 0
        while i < len(histogram):
            if not stack or hg[i] >= hg[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                val = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = val * (width)
                if area > maximum:
                    maximum = area

        while len(stack):
            height = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            area = hg[height] * (width)
            if area > maximum:
                maximum = area
        return maximum

    max_all = 0
    M = generate_histograms(M)
    if not M:
        return 0
    for histogram in M:
        max_row = get_max_area(histogram)
        if max_row > max_all:
            max_all = max_row
    return max_all


def lis(arr):
    n = len(arr)
    # Declare the list (array) for LIS and initialize LIS values for all indexes
    lis1 = [1] * n
    lis2 = [1] * n
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis1[i] < lis1[j] + 1:
                lis1[i] = lis1[j] + 1
    max1 = max(0, max(lis1))

    for i in range(n-2, 0, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and lis2[i] < lis2[j] + 1:
                lis2[i] = lis2[j] + 1
    max2 = max(0, max(lis2))
    return max1+max2


# Driver program to test above function
arr = [1, 11, 2, 10, 4, 5, 2, 1]
print("Length of lis is", lis(arr))
