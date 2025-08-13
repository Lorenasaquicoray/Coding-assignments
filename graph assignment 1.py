# This is a graph represented using an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [7],
    6: [8],
    7: [9],
    8: [10],
    9: [11],
    10: [12],
    11: [12],
    12: []
}

# Depth-First Search (DFS) to find a path from start to goal
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []  # start with an empty path
    path = path + [start]  # add the current node to path

    if start == goal:
        return path  # found the goal

    if start not in graph or not graph[start]:
        return None  # dead end

    for neighbor in graph[start]:
        if neighbor not in path:  # avoid cycles
            result = dfs(graph, neighbor, goal, path)
            if result is not None:
                return result  # return path if found

    return None  # no path found


from collections import deque

# Breadth-First Search (BFS) to find shortest path from start to goal
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # queue holds (current_node, path_to_node)

    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path  # found the goal
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))  # enqueue new path

    return None  # no path found

# Test DFS and BFS for a few target nodes
nodes_in_graph = [7, 12]
node_not_in_graph = 20  # not in graph
testing_nodes = nodes_in_graph + [node_not_in_graph]

for method, fun in [("DFS", dfs), ("BFS", bfs)]:
    print(f"\n{method}:")
    for target in testing_nodes:
        result = fun(graph, 1, target)
        print(f"Path from 1 to {target}: {result}")

# Topological Sort: gives order of tasks based on dependencies
def topological_sort(graph):
    visited = set()
    stack = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(neighbor)
            stack.insert(0, node)  # add to front of stack (post-order)

    for node in graph:
        visit(node)

    return stack

print("Topological order:", topological_sort(graph))


# Strongly Connected Components (SCCs) using Kosaraju's Algorithm
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # adjacency list
        self.V = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)  # add directed edge

    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited, component)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order_
