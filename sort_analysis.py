import time
import tracemalloc
import random
import matplotlib.pyplot as plt

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Measure Performance
def measure_performance(sort_function, data):
    tracemalloc.start()
    start_time = time.time()
    sort_function(data.copy())  # use a copy to avoid in-place effects
    end_time = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024  # time in seconds, memory in KB

# Test Configurations
sizes = [100, 1000, 5000]
results = {
    "Merge Sort": {"time": [], "memory": []},
    "Quick Sort": {"time": [], "memory": []}
}

# Run Tests
for size in sizes:
    data = random.sample(range(size * 10), size)
    for name, func in [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]:
        time_taken, memory_used = measure_performance(func, data)
        results[name]["time"].append(time_taken)
        results[name]["memory"].append(memory_used)

# Plot Results
plt.figure(figsize=(12, 5))

# Time Comparison
plt.subplot(1, 2, 1)
plt.plot(sizes, results["Merge Sort"]["time"], label="Merge Sort", marker='o')
plt.plot(sizes, results["Quick Sort"]["time"], label="Quick Sort", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison")
plt.legend()

# Memory Comparison
plt.subplot(1, 2, 2)
plt.plot(sizes, results["Merge Sort"]["memory"], label="Merge Sort", marker='o')
plt.plot(sizes, results["Quick Sort"]["memory"], label="Quick Sort", marker='o')
plt.xlabel("Input Size")
plt.ylabel("Memory Usage (KB)")
plt.title("Memory Usage Comparison")
plt.legend()

plt.tight_layout()
plt.show()
