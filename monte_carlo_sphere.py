import numpy as np
import time
from multiprocessing import Pool

total_points = 10000000


def calculate_sphere_volume(total_points):
    inside_count = 0
    iterations = 0

    rng = np.random.default_rng(time.time_ns())

    while iterations < total_points:
        # random x, y, and z between -1 and 1
        x, y, z = (
            rng.uniform(-1, 1),
            rng.uniform(-1, 1),
            rng.uniform(-1, 1),
        )

        if x * x + y * y + z * z <= 1:
            inside_count += 1  # if inside, increment inside count by 1

        iterations += 1  # Increment iteration count

        cube_volume = 2 * 2 * 2  # Volume of the cube
        volume_approx = (inside_count / total_points) * cube_volume

    return volume_approx


if __name__ == "__main__":
    start_time = time.time()
    num_processes = 8  # Number of processes

    chunk_size = total_points // num_processes

    # Create a pool of processes and divide the total work among them
    with Pool(num_processes) as p:
        results = p.map(calculate_sphere_volume, [chunk_size] * num_processes)

    # Combine the results from all processes
    # inside_count_total = sum(results)
    # cube_volume = 2 * 2 * 2  # Volume of the cube
    # volume_approx = (inside_count_total / total_points) * cube_volume

    volume_final = sum(results) / num_processes
    print("Approximate volume of sphere:", volume_final)
    end_time = time.time()  # End time for multiprocessing
    print("Time taken by multiprocessing:", end_time - start_time)

    print("-----------------------------")

    print("Accuracy:")
    theoretical_val = 4.18879
    accuracy_percent = (volume_final / theoretical_val) * 100
    print("Theoretical value is:", theoretical_val)
    print("Generate value:", volume_final)
    print("Difference in values:", theoretical_val - volume_final)
    print("Accuracy of this process:", accuracy_percent)
