import numpy as np
import time

total_points = 1000000

def calculate_sphere_volume(total_points):
    inside_count = 0
    iterations = 0

    rng = np.random.default_rng(time.time_ns())

    while iterations < total_points:
        # random x y and z  between 1 nd -1
        x, y, z = (
            rng.uniform(-1, 1),
            rng.uniform(-1, 1),
            rng.uniform(-1, 1),
        )

        if x**2 + y**2 + z**2 <= 1:
            inside_count += 1  # if inside increment inside count by 1

        iterations += 1  # at end of while loop increment the no of iteration we are on

    # volume calculation
    cube_volume = 2 * 2 * 2
    volume_approx = (inside_count / total_points) * cube_volume
    print("Approximate volume of sphere is: ", volume_approx)

if __name__ == "__main__":
    calculate_sphere_volume(total_points)
