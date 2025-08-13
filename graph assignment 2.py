from collections import deque
import random

# BFS to find augmenting path in residual graph
def bfs(capacity, residual_graph, source, sink, parent):
    visited = set()           # Track visited nodes
    queue = deque([source])   # BFS queue starting at source
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in capacity[u]:
            # If v not visited and residual capacity > 0, it's part of augmenting path
            if v not in visited and capacity[u][v] - residual_graph[u].get(v, 0) > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u  # Store path
                if v == sink:  # Stop if sink reached
                    return True
    return False

# Ford-Fulkerson algorithm to compute max flow from source to sink
def ford_fulkerson(graph, source, sink):
    capacity = {}         # Stores capacities of edges
    residual_graph = {}   # Stores current flow along edges
    parent = {}           # To reconstruct augmenting path

    # Collect all nodes from graph keys and adjacency lists
    nodes = set(graph.keys())
    for u in graph:
        nodes.update(graph[u].keys())

    # Initialize capacity and residual graph dictionaries for all nodes
    for u in nodes:
        capacity[u] = {}
        residual_graph[u] = {}

    # Populate capacity and initialize residual flows to zero
    for u in graph:
        for v in graph[u]:
            capacity[u][v] = graph[u][v]
            if v not in capacity:
                capacity[v] = {}
            if u not in capacity[v]:
                capacity[v][u] = 0  # Reverse edges start with zero capacity

            residual_graph[u][v] = 0
            residual_graph[v][u] = 0

    max_flow = 0

    # While there exists an augmenting path, increase flow along it
    while bfs(capacity, residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink

        # Find minimum residual capacity along the path found by BFS
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - residual_graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities along the path
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] += path_flow  # Forward edge increases flow
            residual_graph[v][u] -= path_flow  # Reverse edge decreases flow
            v = parent[v]

        max_flow += path_flow  # Add path flow to total max flow

    return max_flow


# Example graph (manually defined)
graph1 = {
    's': {'a': 4, 'b': 2},
    'a': {'b': 1, 'c': 2, 'd': 4},
    'b': {'d': 2},
    'c': {'t': 3},
    'd': {'t': 3},
    't': {}
}

max_flow_1 = ford_fulkerson(graph1, 's', 't')
print("Maximum flow from s to t in Graph 1:", max_flow_1)


# Function to generate a random directed graph with capacities
def generate_random_graph(num_nodes, edge_probability=0.3, min_capacity=1, max_capacity=10):
    nodes = [chr(97 + i) for i in range(num_nodes)]  # e.g., 'a', 'b', 'c', ...
    graph = {node: {} for node in nodes}

    # Randomly add edges with given probability and capacities
    for u in nodes:
        for v in nodes:
            if u != v and random.random() < edge_probability:
                graph[u][v] = random.randint(min_capacity, max_capacity)

    return graph

graph2 = generate_random_graph(8)
source2 = 'a'
sink2 = 'h'  # Corrected extra space after 'h'

# Make sure source and sink are in the graph, even if isolated
graph2.setdefault(source2, {})
graph2.setdefault(sink2, {})

max_flow_2 = ford_fulkerson(graph2, source2, sink2)
print("Maximum flow from a to h in Random Graph:", max_flow_2)

print("Graph 2 structure:")
for u in graph2:
    for v in graph2[u]:
        print(f"{u} -> {v}: {graph2[u][v]}")
