"""
x=['banana', 'apple', 'kivi']
y=['banana', 'apple', 'kivi']
z=x
y=z
print(x is z)
print(x is not y) # False - because even they have same content, x is not the same as y
print(x==y)  
print(y is z)
"""

x=['pear', 'bmw', 'sofa']
y=['pear', 'bmw', 'sofa']
print(x is not y)
z=x
print(x is z)