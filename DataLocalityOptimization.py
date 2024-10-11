import numpy as np
import time

# Naive implementation: Using a Python list
def naive_implementation(data):
    result = []
    for i in range(len(data) - 1):
        # Each access to `data[i]` and `data[i + 1]` may not be contiguous in memory
        result.append(data[i] + data[i + 1])
    return result

# Optimized implementation: Using a NumPy array for contiguous memory access
def optimized_implementation(data):
    # Using NumPy's in-place operations for contiguous memory access
    return data[:-1] + data[1:]

# Generate a large dataset for performance testing
data_list = [np.random.rand() for _ in range(1000000)]
data_array = np.array(data_list)

# Timing the naive implementation
start_time = time.time()
naive_result = naive_implementation(data_list)
naive_duration = time.time() - start_time
print(f"Naive implementation time: {naive_duration:.4f} seconds")

# Timing the optimized implementation
start_time = time.time()
optimized_result = optimized_implementation(data_array)
optimized_duration = time.time() - start_time
print(f"Optimized implementation time: {optimized_duration:.4f} seconds")

# Verify that both implementations produce the same results
print("Results match:", np.allclose(naive_result[:10], optimized_result[:10]))

# Performance Improvement
improvement = (naive_duration - optimized_duration) / naive_duration * 100
print(f"Performance improvement: {improvement:.2f}%")
