def findMin(ary):

    def recurse(lo, hi):
        # Base cases
        if ary[lo] < ary[hi]:
            return ary[lo]
        elif hi - lo == 1:
            return ary[hi]  ## just return a number, don't call min()
        else:
            mid = lo + (hi - lo) // 2
            if ary[mid] < ary[hi]:
                return recurse(lo, mid)
            else:
                return recurse(mid, hi)
    return recurse(0, len(ary) - 1)


ary = (3, 4, 5, 6, 7, 1, 2)
print(findMin(ary)) # 1
