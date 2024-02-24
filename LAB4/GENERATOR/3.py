def divisible_by_3_and_4(n):
  num = 12

  while num <= n:
    yield num
    num += 12

for num in divisible_by_3_and_4(100):
  print(num)