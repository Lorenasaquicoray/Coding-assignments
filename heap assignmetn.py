import heapq
import time
import random

def buildheap1 (elements):
    heap = []
    for a in elements:
        heapq.heappush(heap,a)
    return heap
def buildheap2 (elements):
    heap = elements[:]
    heapq.heapify(heap)
    return heap

def executiontimes (t):
    times = []
    sets = {
        "smallest to largest": list(range(t)),
        "largest to smallest": list(range(t-1,-1,-1)),
        "randomized":random.sample(range(t),t)
    }
    for name,elements in sets.items():
        start = time.time()
        buildheap1(elements)
        one_by_one = time.time()-start

        start = time.time()
        buildheap2(elements)
        all_same_time = time.time() - start

        #source: stack overflow https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
        times.append((name,one_by_one,all_same_time))
    return times

if __name__ == "__main__":
    I = 200000
    results = executiontimes(I)

    for name, one_by_one, all_at_once in results:
        print(f"For input type '{name}':")
        print(f" Time for one by one: {one_by_one:.6f} seconds")
        print(f" Time for all at once: {all_at_once:.6f} seconds\n")