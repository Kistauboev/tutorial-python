def solve(num_heads, num_legs):
    num_rabbits = (num_legs - (2 * num_heads)) / 2
    num_chickens = num_heads - num_rabbits
    return int(num_chickens), int(num_rabbits)

num_heads = 35
num_legs = 94
chickens, rabbits = solve(num_heads, num_legs)

print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)
