def grams_to_ounces(grams):
    ounces = grams * 28.3495
    return ounces

# Example1:
grams_needed = 100
ounces_needed = grams_to_ounces(grams_needed)
print(ounces_needed)
# Example 2:
gram_1 = 200
ounce_1 = grams_to_ounces(gram_1)
print(ounce_1)
