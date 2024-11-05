import numpy as np


total_points = 1000000  
inside_count = 0        
iterations = 0        
area_of_square = 2*2


while iterations < total_points:
    # Generate random x, y coordinates between -1 and 1
    x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    
    # Check if the point is inside the unit disk
    if x**2 + y**2 <= 1:
        inside_count += 1  # Increment count if point is inside
    
    iterations += 1  # Increment the number of iterations

# Calculate the area of the unit disk approximation
area_approximation = (inside_count / total_points) * (area_of_square)
print("Approximated area of the unit disk:", area_approximation)
