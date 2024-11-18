import numpy as np
import matplotlib.pyplot as plt

#total_points = 1000000

def calculate_unitdisk_area(total_points):
    inside_count = 0
    iterations = 0
    area_of_square = 2 * 2

    while iterations < total_points:
        # Generate random x, y coordinates between -1 and 1
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)

        # Check if the point is inside the unit disk
        if x**2 + y**2 <= 1:
            inside_count += 1  # Increment count if point is inside

        iterations += 1  # Increment the number of iterations

    # Calculate the area of the unit disk approximation
    area_approximation = (inside_count / total_points) * (area_of_square)
    #print("Approximated area of the unit disk:", area_approximation)
    return area_approximation

def iterate_through_total_points(max_points):
    max_exp = np.floor(np.log10(max_points))
    exp_range = np.arange(0, max_exp+1, 0.1)
    point_range = 10**exp_range

    areas = np.empty_like(point_range)
    for i,n in enumerate(point_range):
        area_n = calculate_unitdisk_area(np.floor(n))
        areas[i] = area_n

    fig = plt.figure()
    plt.plot(point_range, areas, label = "Approximation")
    plt.axhline(np.pi, c='black', linestyle='dashed', label="True Value")
    plt.xscale('log')
    plt.grid()
    plt.title("Area of disk versus number of iterations")
    plt.xlabel("Number of iterations")
    plt.ylabel("Area")
    plt.legend(loc="upper right")
    plt.savefig("unitdisk_area_vs_iterations.png")
    plt.close()

    fig = plt.figure()
    plt.plot(point_range, np.abs(areas - np.pi))
    plt.xscale('log')
    plt.grid()
    plt.title("Absolute error in approximation of unit disk area")
    plt.xlabel("Number of iterations")
    plt.ylabel("Absolute error")
    plt.savefig("unitdisk_error_vs_iterations.png")
    plt.close()

    fig = plt.figure()
    plt.plot(point_range[:-1], np.abs(areas[1:] - areas[:-1]))
    plt.xscale('log')
    plt.grid()
    plt.title("Relative error in approximation of unit disk area")
    plt.xlabel("Number of iterations")
    plt.ylabel("Relative error")
    plt.savefig("unitdisk_rel_error_vs_iterations.png")
    plt.close()

if __name__ == "__main__":
    #calculate_unitdisk_area(total_points)
    iterate_through_total_points(10000)