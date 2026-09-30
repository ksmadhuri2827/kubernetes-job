import numpy as np
import platform
import time

print("================================")
print("Scientific Computing Demo")
print("================================")

print("Starting AbbVie scientific computing workload...")

print("Operating System:", platform.system())
print("Python Environment Running")

start_time = time.time()

print("Creating matrices...")

matrix_a = np.random.rand(2000, 2000)
matrix_b = np.random.rand(2000, 2000)

print("Running matrix multiplication...")

result = np.dot(matrix_a, matrix_b)

end_time = time.time()

print("Calculation completed")
print("Result shape:", result.shape)
print("Execution time:", round(end_time - start_time, 2), "seconds")