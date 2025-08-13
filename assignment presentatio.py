import itertools

# List of edges in the graph (each edge connects two vertices)
edges = [(1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4)]

# Create a set of all unique vertices from the edges
vertices = set()
for a, b in edges:
    vertices.add(a)
    vertices.add(b)

# Check if a given set of vertices 'vertex' covers all edges
# That means every edge has at least one endpoint in 'vertex'
def vertex(vertex, edges):
    for a, b in edges:
        # If neither endpoint of this edge is in the vertex set, return False
        if a not in vertex and b not in vertex:
            return False
    # All edges have at least one endpoint in the vertex set
    return True

# Check if there exists a vertex cover of size k
def vertex_k(vertices, edges, k):
    # Try all combinations of vertices of size k
    for subset in itertools.combinations(vertices, k):
        if vertex(subset, edges):
            return True, subset  # Found a vertex cover of size k
    return False, []  # No vertex cover of size k found

# Test function to check vertex cover of size 3 in the example graph
def test():
    edges = [(1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4)]
    vertices = {1, 2, 3, 4}
    k = 3  # looking for vertex cover of size 3

    result, cover = vertex_k(vertices, edges, k)
    print("Vertex Cover Found?", result)
    print("Vertices used:", cover)

test()



