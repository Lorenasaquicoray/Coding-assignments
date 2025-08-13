#sources https://www.geeksforgeeks.org/dsa/0-1-knapsack-problem-dp-10/
#https://www.w3schools.com/dsa/dsa_ref_knapsack.php

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]


    w = capacity
    items_used = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_used.append(i - 1)
            w -= weights[i - 1]

    max_value = dp[n][capacity]
    return max_value, items_used

values1 = [1, 6, 18, 22, 28]
weights1 = [1, 2, 5, 6, 7]
capacity1 = 11

max_val1, items_used1 = knapsack(values1, weights1, capacity1)

print("Max Value:", max_val1)
print("Items Used: ") #0 base index
for i in items_used1:
    print(f"Item {i + 1}: Value = {values1[i]}, Weight = {weights1[i]}")


values2 = [
    16808, 50074, 8931, 27545, 77924, 64441, 84493, 7988, 82328, 78841,
    44304, 17710, 29561, 93100, 51817, 99098, 13513, 23811, 80980, 36580,
    11968, 1394, 25486, 25229, 40195, 35002, 16709, 15669, 88125, 9531,
    27723, 28550
]
weights2 = [
    250, 659, 273, 879, 710, 166, 43, 504, 730, 613,
    170, 158, 934, 279, 336, 827, 268, 634, 150, 822,
    673, 337, 746, 92, 358, 154, 945, 491, 197, 904,
    667, 25
]
capacity2 = 10000

max_val2, items_used2 = knapsack(values2, weights2, capacity2)

print("Max Value:", max_val2)
print("Items Used:") #0 base index
for i in items_used2:
    print(f"Item {i + 1}: Value = {values2[i]}, Weight = {weights2[i]}")

