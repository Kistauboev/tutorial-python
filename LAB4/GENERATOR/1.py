def gensquares(N):
  for i in range(1, N + 1):
    yield i * i
n=int(input())
for square in gensquares(n):
  print(square)