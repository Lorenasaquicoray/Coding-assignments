import itertools
import time
import random
import matplotlib.pyplot as plt


# Brute-force solution for TSP
def tsp_brute_force(graph):
    N = len(graph)  # Number of cities
    min_cost = float('inf')  # Start with infinite cost
    best_path = []  # Best route found so far

    # Generate all possible orders to visit cities except city 0
    for perm in itertools.permutations(range(1, N)):
        # Complete path starts and ends at city 0
        path = (0,) + perm + (0,)

        # Calculate total distance for this path
        cost = sum(graph[path[i]][path[i + 1]] for i in range(N))

        # Update best path if current cost is less
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return min_cost, best_path


# Held-Karp dynamic programming solution for TSP
def solve_tsp_held_karp_dp(dist_matrix):
    n = len(dist_matrix)  # Number of cities
    dp = {}  # Dictionary to store minimum costs for subsets

    # Initialize dp with distances from city 0 to each other city
    for k in range(1, n):
        dp[(1 << k, k)] = dist_matrix[0][k]

    # Consider subsets of increasing size
    for subset_size in range(2, n):
        # For each subset of cities (excluding city 0)
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = sum(1 << x for x in subset)  # Bitmask for subset

            # For each city k in the subset, find min cost path to k
            for k in subset:
                prev_bits = bits & ~(1 << k)  # Remove k from subset

                # Minimum cost to reach k from any other city m in subset
                dp[(bits, k)] = min(
                    dp[(prev_bits, m)] + dist_matrix[m][k]
                    for m in subset if m != k
                )

    bits = (1 << n) - 2  # Bitmask for all cities except 0
    # Find minimum cost to return to city 0 after visiting all cities
    return min(dp[(bits, k)] + dist_matrix[k][0] for k in range(1, n))


# Test both methods with different numbers of cities and measure times
sizes = [4, 5, 6, 7, 8, 9, 10, 11, 12]
brute_times = []
dp_times = []

print("Measuring execution times...")

for N in sizes:
    print(f"Running for N = {N} cities")

    # Create random distance matrix for N cities (0 distance to itself)
    graph = [[random.randint(10, 100) if i != j else 0 for j in range(N)] for i in range(N)]

    # Run brute force only for small N (<=10)
    if N <= 10:
        start = time.time()
        tsp_brute_force(graph)
        elapsed = time.time() - start
        brute_times.append(elapsed)
        print(f"  Brute Force: {elapsed:.4f}s")
    else:
        brute_times.append(None)
        print(f"  Brute Force: skipped")

    # Run Held-Karp dynamic programming for all N
    start = time.time()
    solve_tsp_held_karp_dp(graph)
    elapsed = time.time() - start
    dp_times.append(elapsed)
    print(f"  Held-Karp DP: {elapsed:.4f}s")

# Plot execution time comparison
plt.figure()

# Plot brute force times (red line, circles)
plt.plot(
    [n for n in sizes if brute_times[sizes.index(n)] is not None],
    [t for t in brute_times if t is not None],
    color='red',
    marker='o',
    label='TSP solver (Brute Force)'
)

# Plot Held-Karp DP times (green line, squares)
plt.plot(
    sizes,
    dp_times,
    color='green',
    marker='s',
    label='Held-Karp Algorithm (DP)'
)

plt.xlabel('N (Number of Cities)')
plt.ylabel('Execution Time (seconds)')
plt.title('TSP Execution Time Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
