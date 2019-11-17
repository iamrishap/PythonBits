def maxDifference(a):
    n = len(a)
    if n < 2:
        return -1
    diff = a[1] - a[0] if a[1] - a[0] > 0 else -1
    if n == 2:
        return diff
    max_sum = now_sum = diff
    for i in range(1, n-1):
        diff = a[i+1] - a[i]
        now_sum = diff if now_sum <= 0 else now_sum + diff # if negative, rather exclude
        max_sum = max(max_sum, now_sum)
    return max_sum

# if now_sum > 0:
#     now_sum += diff
# else:
#     now_sum = diff
