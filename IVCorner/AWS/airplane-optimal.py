def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    from heapq import heappush, heappop
    heap, result = [], []
    visited = set()
    # Index of forward route, index of return route, max distance found so far
    iF, iR, maxDistFound = 0, 0, 0
    forwardRouteList.sort(key=lambda x: x[1], reverse=True)
    returnRouteList.sort(key=lambda x: x[1], reverse=True)
    visited.add((0, 0))
    heappush(heap, (-1 * (forwardRouteList[0][1] + returnRouteList[0][1]), (0, 0)))
    while len(heap) > 0:
        sum, (iF, iR) = heappop(heap)
        if maxDistFound < -1 * sum < maxTravelDist:
            result = [[iF, iR]]
            maxDistFound = -1 * sum
        elif -1 * sum == maxTravelDist:
            result.append([iF, iR])
        if (iF + 1, iR) not in visited and iF < len(forwardRouteList) - 1:
            heappush(heap, (-1 * (forwardRouteList[iF + 1][1] + returnRouteList[iR][1]), (iF + 1, iR)))
            visited.add((iF + 1, iR))
        if (iF, iR + 1) not in visited and iR < len(returnRouteList) - 1:
            heappush(heap, (-1 * (forwardRouteList[iF][1] + returnRouteList[iR + 1][1]), (iF, iR + 1)))
            visited.add((iF, iR + 1))
    return result


# maxTravelDist = 7000
# forwardRouteList = [[1, 2000], [2, 4000], [3, 6000]]
# returnRouteList = [[1, 2000]]
# print(optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList))

maxTravelDist = 25
forwardRouteList = [[1, 8], [2, 7], [3, 14]]
returnRouteList = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList))
