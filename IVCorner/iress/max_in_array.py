'''
A function that finds the number that occurs most often in the array. In case of a clash, it returns either one of them.
Input : M (max number value in array), array of N numbers (each number <= M)
'''

def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp >= maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]


print(solution(6,[3,2,2,2,3,6,5,1,5,1]))

