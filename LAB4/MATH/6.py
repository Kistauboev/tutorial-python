def calculate_trapezoid_area(base1, base2, height):
  if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or not isinstance(height, (int, float)):
    raise ValueError("All inputs must be numeric values.")

  if base1 <= 0 or base2 <= 0 or height <= 0:
    raise ValueError("All inputs must be positive numbers.")
  area = (base1 + base2) * height / 2

  return area

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

try:
  area = calculate_trapezoid_area(base1, base2, height)
  print(f"Expected output: {area:.1f}")
except ValueError as e:
  print(f"Error: {e}")