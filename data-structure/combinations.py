def printList(alist):
    print(''.join(alist))


def printUniqueCombinations(alist, numb, blist=[]):
    if not numb:
        return printList(blist)
    for i in range(len(alist)-numb+1):  # loop till only len(numb) is left in the alist
        blist.append(alist[i])  # add this to combinations and check the alist further for rest of the values
        printUniqueCombinations(alist[i+1:], numb-1, blist)
        blist.pop()


def printCombinations(alist, numb, blist=[]):
    if not numb:
        return printList(blist)
    for i in range(len(alist)):
        blist.append(alist.pop(i))  # add this to combinations blist and remove from alist
        printCombinations(alist, numb-1, blist)
        alist.insert(i, blist.pop())  # add this back to alist and remove from blist


print(printUniqueCombinations(list('rishap'), 3))
print(printCombinations(list('rishap'), 3))
