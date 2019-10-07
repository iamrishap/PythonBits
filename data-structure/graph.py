import doctest

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    '''
    >>> dfs(graph, 'A')
    ['A', 'B', 'E', 'F', 'C', 'D']
    '''
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited


def bfs(graph, start):
    '''
    >>> bfs(graph, 'A')
    ['A', 'B', 'C', 'E', 'D', 'F']
    '''
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)  # leftmost
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

doctest.testmod()
