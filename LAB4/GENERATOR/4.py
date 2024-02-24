def squares(a, b):
  if not isinstance(a, int) or not isinstance(b, int):
    raise ValueError("a and b must be integers.")

  if a > b:
    raise ValueError("a must be less than or equal to b.")

  for i in range(a, b + 1):
    yield i * i

a = 'ali'
b = 'muhit'

for square in squares(a, b):
  print(square)