def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)
    for node in graph[vertex]:
        if node not in visited:
            dfs_recursive(graph, node, visited)


def dfs_iterative(graph, vertex):
    visited = set()
    s = list()
    s.append(vertex)
    while len(s) > 0:
        x = s.pop()
        print(x)
        visited.add(x)
        for node in graph[x]:
            if node not in visited and node not in s:
                s.append(node)


graph = {"0": set(["1", "2"]),
         "1": set(["0", "3", "4"]),
         "2": set(["0", "4"]),
         "3": set(["1", "4"]),
         "4": set(["1", "2", "3"])}

dfs_recursive(graph, "0")
dfs_iterative(graph, "0")
