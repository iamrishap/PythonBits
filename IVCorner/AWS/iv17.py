def ways_to_sum(A, amount, path=[], used_denom={}):
    if not A or amount < 0:
        return
    if amount == 0:
        if len(path) > 0 and tuple(sorted(path)) not in used_denom:
            used_denom[tuple(sorted(path))] = True
        return
    for i in A:
        if i <= amount:
            path.append(i)
            ways_to_sum(A, amount-i, path)
    return used_denom


def ways_to_sum_new(A, amount):
    from itertools import combinations
    total_ways = 0
    for i in range(1, len(A) + 1):
        ways = [comb for comb in combinations(A, i) if sum(comb) == amount]
        if ways:
            print(ways)
            total_ways += len(ways)
    print(total_ways)


# print(ways_to_sum([1, 2, 5], 5))
ways_to_sum_new([1, 2, 4, 3, 5], 5)
