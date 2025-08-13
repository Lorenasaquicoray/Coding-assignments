import random

# size of the hash table and number of values to insert
table_size = 10001
num_inserts = 500
mod_hash = 300
c1, c2 = 1, 2  # constants for quadratic probing

# primary hash function: gives a position based on mod 300
def primary_hash(x):
    return x % mod_hash

# secondary hash function used in double hashing
def secondary_hash(x):
    return 9973 - (x % 9973)

# linear probing insertion
def linear_probe_insert(table, x):
    idx = primary_hash(x)  # get starting index
    collisions = 0
    # if the spot is taken, move to the next one until we find an empty spot
    while table[idx] is not None:
        collisions += 1
        idx = (idx + 1) % table_size  # wrap around if needed
    table[idx] = x  # insert the value
    return collisions  # return how many times we had to move

# quadratic probing insertion
def quadratic_probe_insert(table, x):
    idx = primary_hash(x)  # get starting index
    i = 0
    collisions = 0
    # move using the quadratic formula: idx + c1*i + c2*i^2
    while table[(idx + c1 * i + c2 * i * i) % table_size] is not None:
        collisions += 1
        i += 1
    final_idx = (idx + c1 * i + c2 * i * i) % table_size
    table[final_idx] = x
    return collisions

# double hashing insertion
def double_hash_insert(table, x):
    h1 = primary_hash(x)     # first hash
    h2 = secondary_hash(x)   # second hash (step size)
    i = 0
    collisions = 0
    # move by h2 steps until an empty spot is found
    while table[(h1 + i * h2) % table_size] is not None:
        collisions += 1
        i += 1
    table[(h1 + i * h2) % table_size] = x
    return collisions

# improved linear probing with custom step size
def improved_linear_probe_insert(table, x):
    idx = primary_hash(x)         # get starting index
    collisions = 0
    step = (x % 19) + 1           # custom step to spread values better
    while table[idx] is not None:
        collisions += 1
        idx = (idx + step) % table_size
    table[idx] = x
    return collisions

# run the simulation
def simulate():
    random.seed(42)  # for consistent results every time you run it
    values = [random.randint(1, 100000) for _ in range(num_inserts)]  # generate 500 random numbers

    # create 4 empty hash tables (one for each method)
    tables = [[None] * table_size for _ in range(4)]
    collisions = [0, 0, 0, 0]  # to count collisions for each method

    # insert each value into all 4 tables using different methods
    for val in values:
        collisions[0] += linear_probe_insert(tables[0], val)
        collisions[1] += quadratic_probe_insert(tables[1], val)
        collisions[2] += double_hash_insert(tables[2], val)
        collisions[3] += improved_linear_probe_insert(tables[3], val)

    # print the number of collisions for each method
    print("collisions after inserting 500 values:")
    print(f"linear probing: {collisions[0]}")
    print(f"quadratic probing: {collisions[1]}")
    print(f"double hashing: {collisions[2]}")
    print(f"improved linear probing: {collisions[3]}")

# run the program
if __name__ == "__main__":
    simulate()
