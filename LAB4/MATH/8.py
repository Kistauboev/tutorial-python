import math

def calculate_regular_polygon_area(sides, lenght):
  if sides < 3:
    raise ValueError("Number of sides must be at least 3.")

  if lenght <= 0:
    raise ValueError("Side length must be positive.")

  apothem = lenght / (2 * math.tan(math.pi / sides))

  area = sides * lenght * apothem / 2

  return area

sides = int(input("Input number of sides: "))
lenght = float(input("Input the length of a side: "))


area = calculate_regular_polygon_area(sides, lenght)
print(f"The area of the polygon is:{area:.2f}")