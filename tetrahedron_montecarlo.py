import numpy as np
import time
import math
from multiprocessing import Pool 


total_points = 10000000

def calculate_r_tetra_volume(total_points, lower , upper):
    inside_count = 0
    iterations = 0

    rng = np.random.default_rng(time.time_ns())
    

    while iterations < total_points:
        # random x, y, and z between 0 and root 2

        root_2 = math.sqrt(2)
        x, y, z = (
            rng.uniform(lower, upper),              # considering a tetrahedron with one vertex along the (root_2,root_2,root_2) vertex of a cube 
            rng.uniform(lower, upper),
            rng.uniform(lower, upper),
        )

         # if x*x + y*y + z*z <= 1:
         #   inside_count += 1  # if inside, increment inside count by 1
        
        if ((x**2 + y**2 + (z-root_2)**2 <= 4)   and   (x**2 + (y-root_2)**2 + z**2 <= 4)   and   ((x-root_2)**2 + y**2 + z**2 <= 4 )   and   ((x-root_2)**2 + (y-root_2)**2 + (z-root_2)**2 <= 4 )):      #eqns of spheres as found in prevoius class exercises 
            inside_count += 1
       
        iterations += 1  # Increment iteration count

    cube_volume =  (upper-lower)**3 # Volume of the cube
    volume_approx = (inside_count / total_points) * cube_volume   

    return volume_approx



if __name__ == "__main__":
    start_time = time.time()  
    num_processes = 8  # Number of processes

    lower, upper = -1, 2  # Bounds for the bounding box    //-1,2 give 100 percent accuracy , -0.5 , 1.6 gives about 98 percent accuarcy
    chunk_size = total_points // num_processes

    args = [(chunk_size, lower, upper) for _ in range(num_processes)]

    # Create a pool of processes and divide the total work among them
    with Pool(num_processes) as p:
        results = p.starmap(calculate_r_tetra_volume, args)                #different then p.map   

    volume_final = sum(results)/num_processes
    print("Approximate volume:", volume_final)
    end_time = time.time()  # End time for multiprocessing
    print("Time taken by multiprocessing:", end_time - start_time)

    print("-----------------------------")

    print("Accuracy:")
    theoretical_val = 3.377261864926
    accuracy_percent = (volume_final/theoretical_val) * 100
    print("Theoretical value is:", theoretical_val)
    print("Generated value:" , volume_final)
    print("Difference in values:" , theoretical_val - volume_final)
    print("Accuracy of this process:" , accuracy_percent)

   
