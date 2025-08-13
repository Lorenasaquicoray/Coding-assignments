import random
import time
import itertools
def generate_entris(a):
    n = []
    for _ in range(a):
        start = random.randint(0, 100000)
        end = start + random.randint(1, 1000)
        n.append((start, end))
    return n

def compatible(activity_set):
    sorted_activities = sorted(activity_set, key=lambda x: x[0])
    for i in range(len(sorted_activities) - 1):
        if sorted_activities[i][1] > sorted_activities[i + 1][0]:
            return False
    return True

def brute_force_activity_selection(n):
    best = []
    for r in range(1, len(n) + 1):
        for subset in itertools.combinations(n, r):
            if compatible(subset) and len(subset) > len(best):
                best = list(subset)
    return best

def greedy_activity_selection(n):
    n.sort(key=lambda x: x[1])
    selected = [n[0]]
    last_end = n[0][1]

    for start, end in n[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def generate_array(n):
    return [random.randint(-1000, 1000) for _ in range(n)]

def brute_force_max_subarray(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum

def divide_and_conquer_maximum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    return max(
        divide_and_conquer_maximum(arr, left, mid),
        divide_and_conquer_maximum(arr, mid + 1, right),
        max_crossing_sum(arr, left, mid, right)
    )

n_activities = 20
activities = generate_entris(n_activities)

start = time.time()
brute = brute_force_activity_selection(activities)
end = time.time()
print(f"Brute Force Selected Activities: {len(brute)}")
print(f"Brute Force Time: {end - start:.4f} seconds")

start = time.time()
greedy = greedy_activity_selection(activities)
end = time.time()
print(f"Greedy Selected Activities: {len(greedy)}")
print(f"Greedy Time: {end - start:.4f} seconds")

n_array = 5000
array = generate_array(n_array)

start = time.time()
brute_sum = brute_force_max_subarray(array)
end = time.time()
print(f"Brute Force Max Subarray Sum: {brute_sum}")
print(f"Brute Force Time: {end - start:.4f} seconds")

start = time.time()
divide_sum = divide_and_conquer_maximum(array, 0, len(array) - 1)
end = time.time()
print(f"Divide & Conquer Max Subarray Sum: {divide_sum}")
print(f"Divide & Conquer Time: {end - start:.4f} seconds")
