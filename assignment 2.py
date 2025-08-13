import math  # Import math module for logarithmic calculation
import time  # Import time module to measure execution time

inputs = [200, 300, 400, 500]

def a(n):
    value = 1.0  # Initial value to compute log on
    for a in range(n):  # Loop runs n times
        # We add a small value (1e-12) to prevent log(0) error and simulate computation
        value = math.log(value + 1e-12) + 6  # Perform logarithmic operation and add 6


def b(n):
    value = 1.0
    for a in range(n):  # Outer loop
        for b in range(n):  # Inner loop: runs n times per outer loop iteration
            # Simulates heavier computation by using nested loops
            value = math.log(value + 1e-8) + 5


def c(n):
    value = 1.0
    for a in range(n):  # Outer loop
        for b in range(a):  # Inner loop runs a times, forming a triangle shape of iterations
            value = math.log(value + 1e-6) + 1  # Simulated computation

# Function d: Same as c() but only computes when b is even, reducing number of operations
def d(n):
    value = 1.0
    for a in range(n):  # Outer loop
        for b in range(a):  # Inner loop
            if b % 2 == 0:  # Compute only for even b values (about half the time)
                value = math.log(value + 1e-10) + 9  # Simulated computation

# Loop through each input size and measure execution time of all functions
for n in inputs:
    print(f"n = {n}")  # Print the current input size being tested


    start = time.time()
    a(n)
    end = time.time()
    print(f"Time a: {end - start:.4f} seconds")


    start = time.time()
    b(n)
    end = time.time()
    print(f"Time b: {end - start:.4f} seconds")


    start = time.time()
    c(n)
    end = time.time()
    print(f"Time c: {end - start:.4f} seconds")


    start = time.time()
    d(n)
    end = time.time()
    print(f"Time d: {end - start:.4f} seconds")

