import math
def area_of_par(base,height):
    if not isinstance(height, (int, float)) or not isinstance(base, (int, float)): 
     raise ValueError("All inputs must be numeric values.")
    area = base * height
    return area
base = float(input("Length of base: "))
height =float(input("Height of parallelogram: "))
area = area_of_par(base , height)
print(f"Expected Output: {area}")